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
    review = models.TextField(max_length=100)
    photo = CloudinaryField('image')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating (1 to 5 stars)"
    )
   # project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='testimonials')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'