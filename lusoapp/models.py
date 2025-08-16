from django.db import models

# Create your models here.
class Clients_logo(models.Model):
    Brand_Name = models.CharField(max_length=100, blank=True, null=True)
    Brand_Logo = models.ImageField(upload_to='clients_logos/', blank=True, null=True)

    def __str__(self):
        return self.Brand_Name if self.Brand_Name else "Client Logo"