from gprojukti_v2.settings.base import DEBUG

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

ON_TOP_APPS = [
    'corsheaders',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    # 'simple_history',
    # 'cacheops',
    'django_filters',
    # 'drf_yasg2',

    'actstream',
    'django_extensions',
    'drf_spectacular',
    'dj_rest_auth.registration',
]

LOCAL_APPS = [
    'base',
    'user',
    'blogs',
    'catalog',
    'products',
    'store',
    # 'supplier',
    # 'campaigns',
    # 'purchase',
    # 'stock',
    # 'promo',
    # 'orders',
    # 'payment',
    'configuration',
    # 'repair',
    # 'pc_builder',
    # 'locations',
    'point_of_sale',

]


INSTALLED_APPS = ON_TOP_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


ON_TOP_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    ]

THIRD_PARTY_MIDDLEWARE = [
    # 'simple_history.middleware.HistoryRequestMiddleware'
    ]

DEFAULT_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOCAL_MIDDLEWARE = [
    # 'base.middleware.AuthMiddleware',
    # 'base.middleware.RequestResponseLogMiddleware',
]

# if DEBUG:
#     THIRD_PARTY_MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
#     import socket
#     hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '192.168.0.164']

MIDDLEWARE = ON_TOP_MIDDLEWARE + DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE

ROOT_URLCONF = 'gprojukti_v2.urls'

WSGI_APPLICATION = 'gprojukti_v2.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'JSON_EDITOR': True,
}