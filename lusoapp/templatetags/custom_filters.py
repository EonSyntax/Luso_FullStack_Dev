from django import template

register = template.Library()

@register.filter
def stars(value):
    try:
        rating = int(value)
        rating = max(1, min(rating, 5))  # Clamp between 1 and 5
        return "⭐" * rating
    except (ValueError, TypeError):
        return "No rating"