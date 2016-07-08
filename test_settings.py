SECRET_KEY = 'ratelimit'

INSTALLED_APPS = (
    'ratelimit',
)

RATELIMIT_USE_CACHE = 'default'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'ratelimit-tests',
    },
    'ratelimit': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 0,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
    'connection-errors': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'test-connection-errors',
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}

# silence system check about unset `MIDDLEWARE_CLASSES`
SILENCED_SYSTEM_CHECKS = ['1_7.W001']
