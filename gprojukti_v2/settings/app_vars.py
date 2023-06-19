import os
from decouple import config
from gprojukti_v2.settings.base import BASE_DIR
from django.utils import timezone
from datetime import date, datetime, timedelta



# django vars
# AUTH_USER_MODEL = 'user.User'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = False

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join('static_cdn', 'static_root')
MEDIA_ROOT = os.path.join('static_cdn', 'media_root')

# env
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASS = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')


REDIS_HOST = config('REDIS_HOST')
RABBITMQ_URL = config('RABBITMQ_URL')
# request setup
REQUEST_TIMEOUT = int(config('REQUEST_TIMEOUT', 8))

# Email
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
FROM_EMAIL = config('FROM_EMAIL')


# AWS s3
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
SECRET_ACCESS_KEY = config('SECRET_ACCESS_KEY')
S3_BUCKET = config('S3_BUCKET')

# SSL ECOMMERCE PAYMENT
SSL_STORE_ID = config('SSL_STORE_ID')
SSL_STORE_PASSWORD = config('SSL_STORE_PASSWORD')
SSL_BASE_URL = config('SSL_BASE_URL')

# Frontend
FRONTEND_BASE_URL = config('FRONTEND_BASE_URL')

# NGORK
NGORK_URL = config('NGORK_URL')

# METABASE
METABASE_SITE_URL = config('METABASE_SITE_URL')
METABASE_SECRET_KEY = config('METABASE_SECRET_KEY')

# DIGITAL OCEAN SPACES
DIGITAL_OCEAN_SPACES_ACCESS_KEY_ID = config('DIGITAL_OCEAN_SPACES_ACCESS_KEY_ID')
DIGITAL_OCEAN_SPACES_SECRET_ACCESS_KEY = config('DIGITAL_OCEAN_SPACES_SECRET_ACCESS_KEY')
DIGITAL_OCEAN_SPACES_ENDPOINT_URL = config('DIGITAL_OCEAN_SPACES_ENDPOINT_URL')
DIGITAL_OCEAN_SPACES_BUCKET_NAME = config('DIGITAL_OCEAN_SPACES_BUCKET_NAME')


# Current Date & Time Check
TODAY = datetime.strptime(
        str(timezone.datetime.now().date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
CURRENT_TIME = timezone.datetime.now().time()
