from django.contrib import admin
from .models import GameName, Role

# Register your models here.
class GameNameInline(admin.StackedInline):
    model = GameName
    extra = 1
admin.site.register(GameName)
admin.site.register(Role)
