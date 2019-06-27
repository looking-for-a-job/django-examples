from django.test import TestCase

"""
https://docs.djangoproject.com/en/2.2/topics/testing/tools/#django.test.SimpleTestCase.modify_settings

redefine settings that contain a LIST OF VALUES
"""

class Test(TestCase):
    def test(self):
        with self.modify_settings(MIDDLEWARE={
                'append': 'django.middleware.cache.FetchFromCacheMiddleware',
                'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
                'remove': [
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                ],
            }):
            pass
