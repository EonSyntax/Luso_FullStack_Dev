from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Clients_logo, Testimonial, Project, BlogPost
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse

# Create your views here.
def index(request):
    reviews = Testimonial.objects.all()
    clientsl = Clients_logo.objects.all().order_by('order')  # Assuming Clients_logo is defined in models.
    projects = Project.objects.prefetch_related('images').all()

    # pass the CATEGORY_CHOICES into template
    categories = Project.CATEGORY_CHOICES

    return render(request, 'pages/index.html', {
        'reviews': reviews,
        'clientsl': clientsl,
        'projects': projects,
        'categories': categories,
    })


def about(request):
    reviews = Testimonial.objects.all()
    return render(request, 'pages/about.html', {
        'reviews': reviews,
    })


def contact(request):
    return render(request, 'pages/contact.html')


def strategy(request):
    return render(request, 'pages/strategy.html')


def blog(request):
    blogs = BlogPost.objects.all()
    return render(request, 'pages/blog.html', {
        'blogs': blogs
    })


def like_blog(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)

    session_key = f"liked_blog_{pk}"
    if not request.session.get(session_key, False):
        blog.likes += 1
        blog.save()
        request.session[session_key] = True  # mark as liked

    return JsonResponse({"likes": blog.likes})





def branding(request):
    return render(request, 'pages/branding.html')


def packages(request):
    return render(request, 'pages/packages.html')

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)

    # 👁 prevent multiple reloads counting as new views
    session_key = f"viewed_blog_{pk}"
    if not request.session.get(session_key, False):
        blog.views += 1
        blog.save()
        request.session[session_key] = True

    # get recent posts (excluding the current one)
    recent_posts = BlogPost.objects.exclude(pk=pk).order_by('-created_at')[:3]

    return render(request, 'pages/blog_detail.html', {
        'blog': blog, 
        'recent_posts': recent_posts
    })


def healthz(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        # database is up
        return HttpResponse("OK", status=200)
    except Exception:
        return HttpResponse("DB Error", status=500)
    

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    reviews = project.testimonials.all()  # thanks to related_name='reviews'
    images = project.images.all()
    return render(request, 'pages/project_detail.html', {
        'project': project,
        'reviews': reviews,
        "images": images,
    })

