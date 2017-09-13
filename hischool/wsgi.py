"""
WSGI config for HiSchool! project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hischool.settings")

# Add the "core" and "extensions" folders to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "extensions"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "core"))

application = get_wsgi_application()
