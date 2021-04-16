from django import template

register = template.Library()


@register.filter()
def get_count(value):
    count = 0
    for i in value:
        count += 1
    return count
