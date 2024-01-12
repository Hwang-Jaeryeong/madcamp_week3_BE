#settings.py
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t+pgn0mo&oi!5ca4$jj-(7@!2d)5a7dsmyfg84-pnji6lne&ur"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # DRF
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    # rest_auth
    'rest_auth',
    'rest_auth.registration',
    'gunicorn',


    # My Apps

]

SITE_ID = 1

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
#AUTH_USER_MODEL = 'accounts.CustomUser'


# JWT 설정
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=28),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# Account and Social Account settings
SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = 'store_list'
ACCOUNT_LOGOUT_REDIRECT_URL = 'store_list'
ACCOUNT_LOGOUT_ON_GET = False
SOCIALACCOUNT_AUTO_SIGNUP = True  # 소셜 로그인 시 자동으로 계정 생성



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "madcamp.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "madcamp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
 #   "default": {
  #      "ENGINE": "django.db.backends.mysql",
  #      "NAME": "cam",
 #       'USER': 'root',
 #       'PASSWORD': 'j20020607',
 #       'HOST': 'localhost',
#        'PORT': '3306',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DATABASE_NAME"),
        'USER': os.environ.get("DATABASE_USERNAME"),
        'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
        'HOST': os.environ.get("DATABASE_HOST"),
        'PORT': int(os.environ.get("DATABASE_PORT", 3306)),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

