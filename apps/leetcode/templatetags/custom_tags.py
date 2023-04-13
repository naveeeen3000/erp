from django import template
register = template.Library()



@register.filter(name='split')
def split_and_return_last(value,key):
    """
    splits the value based on the key.
    """
    return value.split(key)[-1] if value.split(key)[-1] else value.split(key)[-2]