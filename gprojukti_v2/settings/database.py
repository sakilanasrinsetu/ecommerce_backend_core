from gprojukti_v2.settings.base import config, environ, env
from gprojukti_v2.settings.app_vars import DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT, BASE_DIR

if config('DATABASE_URL'):
    DATABASES = {
        'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

# print('DTDTDTDTDTDTDTDTD', DATABASES)