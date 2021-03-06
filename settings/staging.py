from base import *
import os

ALLOWED_HOSTS =[]
DEBUG = False
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
#Facebook settings
SOCIAL_AUTH_FACEBOOK_KEY = '1707059289368051'
SOCIAL_AUTH_FACEBOOK_SECRET = '5207d9dff2f3150b29d36b668f92d85b'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'

#Google settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='228762371032-j80vrqtbvn9jrrrriqnfkn3790f9ulpq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WNEVUBBJKRBVUixdXAwCG0mV'

#Twitter settings
SOCIAL_AUTH_TWITTER_KEY = "hObYTUoxvZMBoQkj4hEFVex0B"
SOCIAL_AUTH_TWITTER_SECRET = "fb242X43722Y5FOKIKYG0v0K7AilDiaK9MBeH4I1xIGIKoSua7"

#Git hub settings
SOCIAL_AUTH_GITHUB_KEY = '276b95f4de367aa1ca82'
SOCIAL_AUTH_GITHUB_SECRET = 'ee58cb791798cf20b7a43c826548284e63c80194'
 
SITE_URL = 'https://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}