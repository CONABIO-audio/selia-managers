import os
from collections import OrderedDict

from irekua_dev_settings.settings import *
from irekua_database.settings import *
from irekua_models.settings import *
from irekua_autocomplete.settings import *
from selia_templates.settings import *
from selia_registration.settings import *
from selia_managers.settings import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

LOGIN_REDIRECT_URL = '/managers'
LOGOUT_REDIRECT_URL = '/managers'

INSTALLED_APPS = list(OrderedDict.fromkeys(
    SELIA_MANAGERS_APPS +
    SELIA_REGISTRATION_APPS +
    SELIA_TEMPLATES_APPS +
    IREKUA_AUTOCOMPLETE_APPS +
    IREKUA_MODELS_APPS +
    IREKUA_DATABASE_APPS +
    IREKUA_BASE_APPS
))
