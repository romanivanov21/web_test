# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_test',
        'USER': 'roman',
        'PASSWORD': 'my password',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
} 