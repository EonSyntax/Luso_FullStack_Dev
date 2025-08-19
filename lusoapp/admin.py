from django.contrib import admin
from django.utils.html import format_html
from .models import Clients_logo, Testimonial

admin.site.site_header = "Luso Site Administration Portal"          # top-left header text
admin.site.site_title = "Luso Site Admin Portal"    # browser tab title
admin.site.index_title = "Welcome to Luso Site Dashboard"  # dashboard index page

class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'



# Register your models here.
@admin.register(Clients_logo)
class Clients_logoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order', 'Brand_Logo')
    ordering = ['order']




@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'star_rating_display' ) # ,'project'
    list_filter = ('rating', ) # ,'project'
    search_fields = ('first_name', 'last_name', 'designation', 'review')


    def star_rating_display(self, obj):
        try:
            return "⭐" * int(obj.rating) if obj.rating else "No rating"
        except (TypeError, ValueError):
            return "Invalid rating"
    star_rating_display.short_description = "Rating"