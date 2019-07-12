from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import GameName, Role
from django.template import loader
# Create your views here.
def index(request):
    temp1 = loader.get_template("game/index.html")
    result = temp1.render({"username": "lwk001"})
    return HttpResponse(result)

    # return HttpResponse('index')
def list(request):
    games = GameName.objects.all()
    return render(request, "game/list.html", locals())
    # roles = Role.objects.all()
    # return render(request, "game/list.html", locals())
    # return HttpResponse('list')
def detail(request,id):

    game = GameName.objects.get(pk=id)
    return render(request, "game/detail.html", locals())
    # return HttpResponse('detail')
