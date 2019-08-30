from django.contrib import admin
from .models import *
# Register your models here.
class AdsAdmin(admin.ModelAdmin):
    list_display = ["desc", "index", "img"]
    list_filter = ["index"]
    list_per_page = 2
    search_fields = ["desc"]
admin.site.register(Ads,AdsAdmin)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
