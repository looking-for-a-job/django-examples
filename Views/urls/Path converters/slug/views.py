from django.http import HttpResponse

def my_view(request,path):
    return HttpResponse("path = %s" % path)
