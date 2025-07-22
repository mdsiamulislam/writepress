"""
Django settings for writepress project.
"""

from pathlib import Path
import os
import dj_database_url # PostgreSQL ডেটাবেজ কনফিগারেশনের জন্য
from decouple import config # এনভায়রনমেন্ট ভ্যারিয়েবল লোড করার জন্য

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY কে Railway Variables এ সেট করতে হবে।
# এটি আপনার প্রোজেক্টের সিকিউরিটির জন্য সবচেয়ে গুরুত্বপূর্ণ।
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG কে Railway Variables এ False সেট করতে হবে।
# প্রোডাকশনে DEBUG True থাকলে আপনার অ্যাপের ভিতরের তথ্য প্রকাশ হতে পারে, যা নিরাপদ নয়।
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS আপনার Railway অ্যাপের URL এবং .railway.app ডোমেইন অন্তর্ভুক্ত করবে।
# 'your-railway-app-name.up.railway.app' এর জায়গায় আপনার Railway প্রজেক্টের আসল ডোমেইন বসাবেন।
# Railway থেকে Deploy করার পর আপনার প্রজেক্টের URL টি Services ট্যাবে পাবেন।
ALLOWED_HOSTS = [
    'your-railway-app-name.up.railway.app',
    '.railway.app',
    '127.0.0.1', # লোকাল ডেভেলপমেন্টের জন্য
    'localhost', # লোকাল ডেভেলপমেন্টের জন্য
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'managepost', # আপনার নিজস্ব অ্যাপ
    # 'whitenoise.runserver_nostatic', # ডেভেলপমেন্টে Whitenoise ব্যবহার করলে এটি যুক্ত করতে পারেন
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # স্ট্যাটিক ফাইল সার্ভ করার জন্য এটি অবশ্যই যুক্ত করুন
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'writepress.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates' # আপনার টেম্পলেট ফোল্ডার যদি রুট প্রজেক্ট ফোল্ডারে থাকে
        ],
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

WSGI_APPLICATION = 'writepress.wsgi.application'


# Database
# Railway-এর ফ্রি টিয়ারে PostgreSQL ডেটাবেজ ব্যবহার করা নিরাপদ এবং ভালো।
# Railway স্বয়ংক্রিয়ভাবে DATABASE_URL ভ্যারিয়েবল তৈরি করবে যখন আপনি একটি PostgreSQL সার্ভিস অ্যাড করবেন।
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}', # লোকাল ডেভেলপমেন্টের জন্য SQLite
        conn_max_age=600 # প্রোডাকশনে ডেটাবেজ কানেকশন পুলিং-এর জন্য
    )
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka' # আপনার টাইম জোন সেট করুন, এটি UTC হতে পারে বা আপনার স্থানীয় টাইম জোন

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static", # আপনার অ্যাপ বা প্রজেক্টের রুট static ফাইলগুলো এখানে
]
# প্রোডাকশনের জন্য সব স্ট্যাটিক ফাইল সংগ্রহ করার ডিরেক্টরি
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise এর মাধ্যমে স্ট্যাটিক ফাইল সার্ভ করার জন্য
# এটি নিশ্চিত করবে যে আপনার CSS, JS ফাইলগুলো প্রোডাকশনে লোড হচ্ছে।
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files (User uploaded files)
# ফ্রি হোস্টিংয়ে ইউজার আপলোড করা মিডিয়া ফাইল সাধারণত সরাসরি ফাইল সিস্টেমে রাখা হয় না।
# কারণ হোস্টিং এনভায়রনমেন্টে ফাইলগুলো স্থায়ী হয় না (ephemeral storage)।
# প্রোডাকশনে মিডিয়া ফাইল সার্ভ করার জন্য AWS S3 বা সমমানের ক্লাউড স্টোরেজ ব্যবহার করা উচিত।
# এটি ফ্রি হয় না, তাই ফ্রি ব্যবহার করতে চাইলে আপাতত এই ফিচারটি বাদ দিতে পারেন অথবা
# লোকাল ডেভেলপমেন্টের জন্য রেখে দিতে পারেন।
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'