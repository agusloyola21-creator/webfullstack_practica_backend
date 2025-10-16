from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = os.environ.get('SECRET_KEY')




DEBUG = env.bool("DEBUG", default=True)


if DEBUG:
    # Entorno de desarrollo
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS_DEV", default=["*"])
    CORS_ALLOWED_ORIGINS = env.list(
        "CORS_ALLOWED_ORIGINS_DEV",
        default=["http://localhost:3000", "http://127.0.0.1:3000"]
    )
    CSRF_TRUSTED_ORIGINS = env.list(
        "CSRF_TRUSTED_ORIGINS_DEV",
        default=["http://localhost:3000"]
    )
else:
    # Entorno de producción (Render + Netlify)
    ALLOWED_HOSTS = env.list(
        "ALLOWED_HOSTS_DEPLOY",
        default=[".onrender.com"]
    )
    CORS_ALLOWED_ORIGINS = env.list(
        "CORS_ALLOWED_ORIGINS_DEPLOY",
        default=["https://gregarious-peony-84c0ff.netlify.app"]
    )
    CSRF_TRUSTED_ORIGINS = env.list(
        "CSRF_TRUSTED_ORIGINS_DEPLOY",
        default=["https://gregarious-peony-84c0ff.netlify.app"]
    )

# Application definition

DJANGO_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APP = [
    'apps.blog',
    'apps.category',
]

THIRD_PARTY_APP = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader'
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APP + THIRD_PARTY_APP


CKEDITOR_UPLOAD_PATH = "/media/"
CKEDITOR_CONFIGS = {
    # 'default': {
    #     'toolbar': 'Custom',
    #     'toolbar_Custom': [
    #         ['Bold', 'Italic', 'Underline'],
    #         ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
    #         ['Link', 'Unlink'],
    #         ['RemoveFormat', 'Source'],
    #     ],
    #     'height': 300,
    #     'width': 300,
    #     'autoParagraph': False
    # },
    'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
}

JAZZMIN_SETTINGS = {
    # otras configuraciones opcionales...

    "show_ui_builder": True,
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "solar",
    "dark_mode_theme": "solar",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'WEBFULLSTACKPRACTICA',
#         'USER' : 'postgres',
#         'PASSWORD' : 'admin',
#         'HOST' : 'localhost',
#         'PORT' : '5432',
#     }
# }



DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}




