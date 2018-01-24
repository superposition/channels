# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-3yt98bfvxe)7+^h#(@8k#1(1m_fpd9x3q2wolfbf^!r5ma62u'

DEBUG = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'chtest',
)

MIDDLEWARE_CLASSES = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'

STATIC_URL = "/static/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        },
    },
}

ALLOWED_HOSTS = ['*']
