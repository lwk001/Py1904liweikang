import xadmin
from .models import *

xadmin.site.register(Ads)
xadmin.site.register(Category)
xadmin.site.register(Product)
xadmin.site.register(Tag)
