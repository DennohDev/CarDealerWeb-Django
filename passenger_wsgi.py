import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project directory to the sys.path
path = '/home/your_username/domains/datacrateauctions.co.ke/public_html'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'cardealer.settings'

# Create `application` callable object
application = get_wsgi_application() 