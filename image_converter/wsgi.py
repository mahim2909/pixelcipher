"""
WSGI config for image_converter project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_converter.settings')

application = get_wsgi_application()
