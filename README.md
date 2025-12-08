# Image Encoder/Decoder Django Application

A web application built with Django that allows you to encode images to base64 text and decode base64 text back to images. The application provides an intuitive user interface for both operations.

## Features

- **Image to Base64 Encoding**: Upload an image and convert it to base64 text
- **Base64 to Image Decoding**: Paste base64 text and convert it back to an image
- **Image Preview**: See previews of both uploaded and decoded images
- **Copy to Clipboard**: Easily copy encoded base64 text
- **Download Decoded Images**: Download decoded images to your computer
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Validates file types and base64 format

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Navigate to the project directory**:
   ```bash
   cd image_converter
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

## Running the Application

1. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

3. The application will be ready to use!

## Usage

### Encoding an Image
1. Click "Choose Image" button to select an image file
2. See the preview of your selected image
3. Click "Encode to Base64" button
4. The base64 encoded text will appear in the output textbox
5. Click "Copy" button to copy the text to your clipboard

### Decoding Base64 to Image
1. Paste or type base64 text in the "Base64 Text Input" field
2. Click "Decode to Image" button
3. The decoded image will appear in the preview
4. Click "Download Image" button to save the image to your computer

## Project Structure

```
image_converter/
├── manage.py
├── requirements.txt
├── README.md
├── image_converter/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── converter/
    ├── migrations/
    ├── templates/
    │   └── converter/
    │       └── index.html
    ├── static/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## API Endpoints

### Encode Image
- **URL**: `/api/encode/`
- **Method**: POST
- **Request**: Multipart form data with 'image' file
- **Response**: JSON with base64_text and data_uri

### Decode Image
- **URL**: `/api/decode/`
- **Method**: POST
- **Request**: JSON with base64_text field
- **Response**: JSON with data_uri and image_format

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)
- And other formats supported by Pillow

## Limits

- Maximum file upload size: 5MB
- Base64 text is limited by browser and server memory

## Security Note

This application is configured for development. For production use:
1. Change the SECRET_KEY in settings.py
2. Set DEBUG = False
3. Configure ALLOWED_HOSTS properly
4. Use a production-grade database
5. Enable HTTPS
6. Set appropriate security headers

## Testing

Run the test suite:
```bash
python manage.py test
```

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, run:
```bash
python manage.py runserver 8080
```

### Database Errors
If you encounter database errors, reset migrations:
```bash
python manage.py migrate --run-syncdb
```

## Browser Compatibility

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is open source and available for educational and personal use.

## Support

For issues or questions, please check the Django documentation at https://docs.djangoproject.com/
