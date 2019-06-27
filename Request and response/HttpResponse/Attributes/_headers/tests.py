from django.http import HttpResponse
from django.test import TestCase



class Test(TestCase):
    def test(self):
        response = HttpResponse()
        print(response._headers)
        for _,t in response._headers.items():
            key, value = t
            print("%s: %s" % (key,value))

