import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serverless_micro_django.settings')
django.setup()

from django.core import management
from django.core.management.commands import makemigrations


management.call_command(makemigrations.Command())
