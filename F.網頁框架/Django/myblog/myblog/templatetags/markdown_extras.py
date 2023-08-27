import markdown
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()



@register.filter(name="convert_makedown")
def convert_makedown(text):
     
    return markdown.markdown(text)


