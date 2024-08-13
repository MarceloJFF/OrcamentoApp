import os
from .settings import *

DEBUG = True
# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'
ALLOWED_HOSTS = ['127.0.0.1']
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'easeapp',
    'USER': 'root',
    'PASSWORD': '1234',
    'HOST': 'localhost',
    'PORT': '3307',
    }
}