from pathlib import Path
import os
from decouple import config
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent
print("DB_LINK from .env:", config("DB_LINK"))

# Security
SECRET_KEY = config("SECRET_KEY1")
DEBUG = config("DEBUG1", cast=bool, default=False)
ALLOWED_HOSTS = ["agriworld.onrender.com", "www.agriworld.com", "localhost", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = [
    "https://agriworld.onrender.com",
    "https://www.agriworld.com",
]

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'sells_core',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config("GOOGLE_CLIENT_ID1"),
            'secret': config("GOOGLE_CLIENT_SECRET1"),
        },
        'AUTH_PARAMS': {
            'access_type': 'online',
            'prompt': 'select_account'
        }
    }
}

# Auth config
ACCOUNT_SIGNUP_FIELDS = ['email', 'username*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_RATE_LIMITS = {"login_failed": "5/m"}
LOGIN_REDIRECT_URL = '/index'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'AgriWorld.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'AgriWorld.wsgi.application'

# Database
# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME1'),
#         'USER': config('DB_USER1'),
#         'PASSWORD': config('DB_PASSWORD1'),
#         'HOST': config('DB_HOST1'),
#         'PORT': config('DB_PORT1', default='5432'),
#     }
# }


DATABASES = {
    'default': dj_database_url.config(default=config("DB_LINK"))
}


# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# i18n
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('hi', 'Hindi'),
    ('ta', 'Tamil'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static/Media
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # your app-level static folder
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
