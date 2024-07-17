from django import template

register = template.Library()

@register.filter
def intspace(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    return f"{value:,}".replace(",", " ")