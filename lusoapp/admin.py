from django.contrib import admin
from .models import Clients_logo

admin.site.site_header = "Luso Site Administration Portal"          # top-left header text
admin.site.site_title = "Luso Site Admin Portal"    # browser tab title
admin.site.index_title = "Welcome to Luso Site Dashboard"  # dashboard index page

class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'



# Register your models here.
admin.site.register(Clients_logo)