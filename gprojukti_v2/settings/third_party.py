from gprojukti_v2.settings import DEBUG, REDIS_HOST, RABBITMQ_URL
from gprojukti_v2.settings.base import timedelta, SECRET_KEY

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    # 'DEFAULT_RENDERER_CLASSES': (
    #     # 'gprojukti_v2.apis.renderers.DefaultRenderer',
    # ),

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    "DEFAULT_PAGINATION_CLASS": "utils.custom_pagination.CustomPagination",

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'DATETIME_FORMAT': '%b %d at %I:%M %P',
    'TIME_FORMAT': '%I:%M %P',
    'PAGE_SIZE': 20

}

# AUTHENTICATION_BACKENDS = [
#     "user.backends.EmailPhoneUsernameAuthenticationBackend"
# ]  # <-- Untested with dj_rest_auth package

# if DEBUG:
#     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] + (
#         # 'gprojukti.apis.renderers.OnlyRawBrowsableAPIRenderer',
#     )
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
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    # "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",  # noqa
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.model.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # cookie
    "AUTH_COOKIE": "access_token",  # Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_DOMAIN": None,  # A string like "example.com", or None for standard domain cookie.
    "AUTH_COOKIE_SECURE": False,  # Whether the auth cookies should be secure (https:// only).
    "AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag.It's not fetch by javascript.
    "AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
    "AUTH_COOKIE_SAMESITE": "Lax",
    # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
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


# DRF Spectacular for api organised view

SPECTACULAR_SETTINGS = {
    "TITLE": "gProjukti API'S",
    "DESCRIPTION": "G-Projukti Online Shopping Destination ",
    "VERSION": "2.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "queryConfigEnabled": True,
        "persistAuthorization": True,
        "tryItOutEnabled": True,
        "displayRequestDuration": True,
    },
    "PARSER_WHITELIST": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],

}