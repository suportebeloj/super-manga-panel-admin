import environ

from supermanga.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list('ALLOWED_HOST')

SECRET_KEY = env('SECRET')