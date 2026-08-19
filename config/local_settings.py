from config.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY='django-insecure-$pa*ar$k350b*f@!o1h-9t)vx9c)xi@+7e=p=@$8#afb9ug#o4'
DEBUG = True