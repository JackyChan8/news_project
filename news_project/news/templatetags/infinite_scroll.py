from django import template

register = template.Library()


@register.inclusion_tag('infinite_scroll.html')
def infinite_scroll():
    return {}
