import os
from django.conf import settings
from open_alchemy import init_yaml
from django_sorcery.db import databases
from django_sorcery.db.url import get_settings

print('alchemy', get_settings('default'))
db = databases.get('default')
SPEC_DIR = os.path.dirname(__file__)
SPEC_FILE = os.path.join(SPEC_DIR, "openapi/openapi.yaml")
MODELS_FILENAME = os.path.join(SPEC_DIR, "models_autogenerated.py")
init_yaml(SPEC_FILE, base=db.Model, models_filename=MODELS_FILENAME)
