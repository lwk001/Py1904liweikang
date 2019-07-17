from django.template import library
register = library.Library()
from mall.models import Product
@register.simple_tag
def getlatestproducts(num=4):
    return Product.objects.order_by("-update_time")[:num]
