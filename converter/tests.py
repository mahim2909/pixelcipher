from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO
import base64


class ImageEncodingDecodingTests(TestCase):
    """Tests for image encoding and decoding functionality"""

    def create_test_image(self):
        """Create a simple test image"""
        img = Image.new('RGB', (100, 100), color='red')
        img_io = BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        return img_io

    def test_encode_image(self):
        """Test image to base64 encoding"""
        img_file = self.create_test_image()
        uploaded_file = SimpleUploadedFile(
            name='test.jpg',
            content=img_file.getvalue(),
            content_type='image/jpeg'
        )

        response = self.client.post('/api/encode/', {'image': uploaded_file})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('base64_text', data)
        self.assertIn('data_uri', data)

    def test_encode_without_image(self):
        """Test encoding without providing an image"""
        response = self.client.post('/api/encode/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('error', data)

    def test_decode_image(self):
        """Test base64 to image decoding"""
        img = Image.new('RGB', (100, 100), color='blue')
        img_io = BytesIO()
        img.save(img_io, 'JPEG')
        base64_text = base64.b64encode(img_io.getvalue()).decode('utf-8')

        response = self.client.post(
            '/api/decode/',
            {'base64_text': base64_text},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('data_uri', data)

    def test_decode_invalid_base64(self):
        """Test decoding with invalid base64"""
        response = self.client.post(
            '/api/decode/',
            {'base64_text': 'invalid_base64!@#$%'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['success'])
