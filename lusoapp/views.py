from django.shortcuts import render

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


