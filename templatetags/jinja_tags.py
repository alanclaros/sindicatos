from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter('get_item')
def get_item(dictionary, key):
    #print('key...', key, '---')
    return dictionary.get(key)


@register.filter('back_class')
def back_class(index):
    if int(index) % 2 == 0:
        return '1'
    else:
        return '2'
