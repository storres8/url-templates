from django import template
register = template.Library()



@register.filter
def cut(value, arg):
    # removes all values from the given string argument
    return value.replace(arg,'')

# register.filter('cut',cut)
# we must register out cut method: 1) what we want to call our method in string fromat
# & 2) the name of the method itself that we just builtself.

# we could also use decorators and just call @register.filter above the method, and this will
# make the methods name the same as the filter name, essentially doing the same thing. 
