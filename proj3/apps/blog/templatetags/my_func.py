# 自定义模板表达式，扩展django原有功能
from django.template import library
from blog.models import Article
register = library.Library()
@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by("-create_time")[:num]


