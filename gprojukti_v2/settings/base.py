from datetime import timedelta
from pathlib import Path
from decouple import config, Csv
import os
import environ
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', default=False, cast=bool)


GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')

CORS_ORIGIN_WHITELIST = [ 'http://144.48.118.78:7777','http://192.168.3.253:3000']

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect

ALLOWED_HOSTS = ['*']

SITE_ID = 1


# CORS_ALLOWED_ORIGINS = [
#     'http://144.48.118.78:7777',
#     'http://192.168.3.253:3000'
# ]

# ACTSTREAM_SETTINGS = {
#     #     'MANAGER': 'account_management.managers.MyActionManager',
#     'FETCH_RELATIONS': True,
#     #     'USE_PREFETCH': True,
#     'USE_JSONFIELD': True,
#     #     'GFK_FETCH_DEPTH': 1,
# }