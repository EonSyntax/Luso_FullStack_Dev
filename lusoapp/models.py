from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.
class Clients_logo(models.Model):
    Brand_Name = models.CharField(max_length=100, blank=True, null=True)
    Brand_Logo = CloudinaryField(
        'image', 
        default="https://res.cloudinary.com/demo/image/upload/sample.jpg"
    )
    Brand_Url = models.URLField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.Brand_Name if self.Brand_Name else "Client Logo"




# Testimonial Section
class Testimonial(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    review = models.TextField(max_length=150)
    photo = CloudinaryField('image')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating (1 to 5 stars)"
    )
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='testimonials')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'



#Project Section
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Branding', 'Branding'),
        ('Strategy Development', 'Strategy Development'),
    ]

    project_name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=200)
    full_description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    launch_date = models.DateField()
    project_url = models.URLField()

    client_name = models.CharField(max_length=100)
    client_brand = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.project.project_name}"
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=300)
    content = models.TextField()
    quote = models.TextField(max_length=300, blank=True, null=True)
    read_time = models.IntegerField("In Minutes", default=1)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default="https://res.cloudinary.com/demo/image/upload/sample.jpg")

    views = models.PositiveIntegerField(default=0)   # 👁
    likes = models.PositiveIntegerField(default=0)   # ❤️

    def __str__(self):
        return self.title