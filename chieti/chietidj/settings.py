# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '5bc%vl)^0jo(9^^ez@)8i&m%7^9$#_yx1=28^lnx9elvg-g6t5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'chieti',
    'allauth',
    'allauth.account',
#    'allauth.socialaccount',
#    'allauth.socialaccount.providers.facebook',
    'django.contrib.admindocs',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chietidj.urls'

WSGI_APPLICATION = 'chietidj.wsgi.application'

#===============================================================================
# 
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#===============================================================================
 
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'chieti_db',
        'USER': 'chieti',
        'PASSWORD': 'django',

        #'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        #'PORT': '3306',
    }
}

ALLOWED_HOSTS=[
    'chietionline.webfactional.com',
    'ex.chietionline.webfactional.com',
    'www.chieticompras.com',
    'chieticompras.com',
]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_DIR = '/home/webapps/static_media'
STATIC_ROOT = '/home/chietionline/webapps/static_media/'

#LOGIN FACEBOOK
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
 
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)
 
# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk',  # instead of 'oauth2'
    }
}
#FIN LOGIN FACEBOOK


#-------------------Para envio de mail 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chietionline@gmail.com'
EMAIL_HOST_PASSWORD = 'wuoleazgkzdvupaf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#-------------------Fin envio mail
