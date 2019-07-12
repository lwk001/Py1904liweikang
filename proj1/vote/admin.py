from django.contrib import admin
from .models import Question, Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
