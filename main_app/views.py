from django.http import HttpResponse


def index(r):
    return HttpResponse("hello world")
