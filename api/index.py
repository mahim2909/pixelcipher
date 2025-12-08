import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_converter.settings')

# Setup Django
django.setup()

# Get the WSGI application
app = get_wsgi_application()
