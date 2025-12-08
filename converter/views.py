from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import base64
import json
import imghdr


def index(request):
    """Main page for image encoding/decoding"""
    return render(request, 'converter/index.html')


@csrf_exempt
@require_http_methods(["POST"])
def encode_image(request):
    """Encode image to base64"""
    try:
        if 'image' not in request.FILES:
            return JsonResponse({
                'success': False,
                'error': 'No image file provided'
            })

        image_file = request.FILES['image']
        
        # Validate image
        image_file.seek(0)
        if not imghdr.what(None, h=image_file.read(32)):
            return JsonResponse({
                'success': False,
                'error': 'File is not a valid image'
            })
        
        # Read and encode the image
        image_file.seek(0)
        image_data = image_file.read()
        base64_encoded = base64.b64encode(image_data).decode('utf-8')
        
        # Determine the image format
        image_format = imghdr.what(None, h=image_data[:32]) or 'jpeg'
        
        # Create data URI
        data_uri = f"data:image/{image_format.lower()};base64,{base64_encoded}"
        
        # Clear memory
        del image_data
        
        return JsonResponse({
            'success': True,
            'base64_text': base64_encoded,
            'data_uri': data_uri,
            'image_format': image_format.lower()
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@csrf_exempt
@require_http_methods(["POST"])
def decode_image(request):
    """Decode base64 to image"""
    try:
        data = json.loads(request.body)
        base64_text = data.get('base64_text', '').strip()
        
        if not base64_text:
            return JsonResponse({
                'success': False,
                'error': 'No base64 text provided'
            })
        
        # Remove data URI scheme if present
        if ',' in base64_text:
            base64_text = base64_text.split(',')[1]
        
        # Decode the base64
        try:
            image_data = base64.b64decode(base64_text)
        except Exception:
            return JsonResponse({
                'success': False,
                'error': 'Invalid base64 format'
            })
        
        # Verify it's a valid image
        if not imghdr.what(None, h=image_data[:32]):
            return JsonResponse({
                'success': False,
                'error': 'Decoded data is not a valid image'
            })
        
        # Determine image format efficiently
        image_format = imghdr.what(None, h=image_data[:32]) or 'jpeg'
        
        # Create data URI for display
        data_uri = f"data:image/{image_format.lower()};base64,{base64_text}"
        
        # Clear memory
        del image_data
        
        return JsonResponse({
            'success': True,
            'data_uri': data_uri,
            'image_format': image_format.lower()
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON format'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
