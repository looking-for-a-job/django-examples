from django.test import TestCase, modify_settings

"""
https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.modify_settings

redefine settings that contain a LIST OF VALUES
"""

@modify_settings(MIDDLEWARE={
        'append': 'django.middleware.cache.FetchFromCacheMiddleware',
        'prepend': 'django.middleware.cache.UpdateCacheMiddleware'
    })
class Test(TestCase):
    @modify_settings(INSTALLED_APPS={'append': "taggit"})
    def test(self):
        pass
