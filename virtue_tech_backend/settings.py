from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------
# FIREBASE KEY PATH
# -----------------------------------------

FIREBASE_KEY_PATH = os.path.join(BASE_DIR, "firebase", "serviceAccountKey.json")


# -----------------------------------------
# SECURITY
# -----------------------------------------

SECRET_KEY = "django-insecure-change-this-key"

DEBUG = False

ALLOWED_HOSTS = [
    "virtue-tech-backend.up.railway.app",
    "virtue-tech-backend-production.up.railway.app",
    "localhost",
    "127.0.0.1",
]


# -----------------------------------------
# INSTALLED APPS
# -----------------------------------------

INSTALLED_APPS = [

    # Django default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",

    # Project apps
    "accounts",
    "courses",
    "bookings",
    "payments",
    "chat",
    "notifications",
    "api",
]


# -----------------------------------------
# MIDDLEWARE
# -----------------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# -----------------------------------------
# URLS
# -----------------------------------------

ROOT_URLCONF = "virtue_tech_backend.urls"


# -----------------------------------------
# TEMPLATES
# -----------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": False,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# -----------------------------------------
# WSGI
# -----------------------------------------

WSGI_APPLICATION = "virtue_tech_backend.wsgi.application"


# -----------------------------------------
# DATABASE
# -----------------------------------------
# (You are using Firebase so no SQL database needed)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# -----------------------------------------
# CUSTOM USER MODEL
# -----------------------------------------

AUTH_USER_MODEL = "accounts.User"


# -----------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -----------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Karachi"

USE_I18N = True
USE_TZ = True


# -----------------------------------------
# STATIC FILES
# -----------------------------------------

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# -----------------------------------------
# MEDIA FILES
# -----------------------------------------

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# -----------------------------------------
# CORS SETTINGS (React Frontend)
# -----------------------------------------

CORS_ALLOWED_ORIGINS = [
    "https://virtue-tech-frontend.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True


# -----------------------------------------
# DJANGO REST FRAMEWORK
# -----------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "accounts.firebase_auth.FirebaseAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}


# -----------------------------------------
# JWT SETTINGS
# -----------------------------------------

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# -----------------------------------------
# DEFAULT PRIMARY KEY
# -----------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"