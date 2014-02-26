from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango Says: Hello, World!")


def about(request):
    return HttpResponse("Rango Says: Here is the about page. Lulz")