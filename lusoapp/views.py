from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request): 
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def strategy(request):
    return render(request, 'pages/strategy.html')


def blog(request):
    return render(request, 'pages/blog.html')


def branding(request):
    return render(request, 'pages/branding.html')


def packages(request):
    return render(request, 'pages/packages.html')


def healthz(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        # database is up
        return HttpResponse("OK", status=200)
    except Exception:
        return HttpResponse("DB Error", status=500)