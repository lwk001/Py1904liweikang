from django.contrib import admin
from .models import *
class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    list_filter = ("title", "pub_date")
    list_per_page = 1
    inlines = [HeroInfoInlines]
#django自带强大的后台管理
# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "content"]
    list_filter = ["name", "content"]
    search_fields = ["name", "content"]

admin.site.register(HeroInfo, HeroInfoAdmin)
