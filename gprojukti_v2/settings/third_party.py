from gprojukti_v2.settings import DEBUG, REDIS_HOST, RABBITMQ_URL
from gprojukti_v2.settings.base import timedelta

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        # 'gprojukti_v2.apis.renderers.DefaultRenderer',
    ),
    "DEFAULT_PAGINATION_CLASS": "utils.custom_pagination.CustomPagination",

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'DATETIME_FORMAT': '%b %d at %I:%M %P',
    'TIME_FORMAT': '%I:%M %P',

}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] + (
        # 'gprojukti.apis.renderers.OnlyRawBrowsableAPIRenderer',
    )
# if not DEBUG:
#     REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'base.exceptions.custom_exception_handler'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_ALLOW_HEADER = [
    'username',
    'group',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_ALLOW_HEADERS = '*'

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://{}:6379/1".format(REDIS_HOST),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "SOCKET_CONNECT_TIMEOUT": 5,
#             "SOCKET_TIMEOUT": 5,
#             "IGNORE_EXCEPTIONS": True,
#             "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
#             "MASTER_CACHE": f"redis://{REDIS_HOST}:6379",
#             "DB": 4,
#         },
#         "KEY_PREFIX": "gprojukti",
#     }
# }

# CACHEOPS_REDIS = "redis://{}:6379/1".format(REDIS_HOST)

# CACHEOPS_DEGRADE_ON_FAILURE = True
# CACHEOPS_ENABLED = True

# CACHEOPS = {
#     'catalog.ProductGroup': {'ops': 'all', 'timeout': 60},
#     'catalog.ProductCategory': {'ops': 'all', 'timeout': 60},
#     'catalog.ProductSubCategory': {'ops': 'all', 'timeout': 60},
#     'catalog.ProductVariant': {'ops': 'all', 'timeout': 60},
# }

# # 5 minutes cache
# CACHE_MIDDLEWARE_SECONDS = 300

# # celery
# CELERY_BROKER_URL = RABBITMQ_URL
# CELERY_RESULT_BACKEND = "redis://{}:6379/".format(REDIS_HOST)
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'
# CELERY_TASK_RESULT_EXPIRES = 3600
# CELERY_TASK_DEFAULT_QUEUE = 'gprojukti.celery'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
  'app_labels': [],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
