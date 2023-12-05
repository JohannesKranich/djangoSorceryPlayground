import os
from polls.models import db
from open_alchemy import init_yaml

SPEC_DIR = os.path.dirname(__file__)
SPEC_FILE = os.path.join(SPEC_DIR, "openapi/openapi.yaml")
MODELS_FILENAME = os.path.join(SPEC_DIR, "models_autogenerated.py")
init_yaml(SPEC_FILE, base=db.Model, models_filename=MODELS_FILENAME)
