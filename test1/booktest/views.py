from django.shortcuts import render,redirect,reverse
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .admin import BookInfo, HeroInfo
from django.views.generic import View, TemplateView

class IndexView(View):
    def get(self, request):
        # 重写get方法，来完成get请求的返回
        pass

# Create your views here.
# def myview(request):
#     return HttpResponse("自定义路由展示页面")
# def youview(request):
#     return HttpResponse('123123')
def index(request):
    # return HttpResponse("首页 <a href='/booktest/list/'>跳到列表</a>")
    temp1 = loader.get_template("booktest/index.html")
    result = temp1.render({"username": "lwk001"})
    return HttpResponse(result)


def list(request):
    # s="""
    # <a href='/detail/1/'>跳转到详情</a>
    # <a href='/detail/2/'>跳转到详情</a>
    # <a href='/detail/3/'>跳转到详情</a>
    # """
    # return HttpResponse("列表 <a href='/booktest/detail/'>跳到详细%</a>")

    temp2 = loader.get_template("booktest/list.html")
    books = BookInfo.objects.all()
    result = temp2.render({"books": books})
    return HttpResponse(result)
def detail(request,id):
    # return HttpResponse("详情 <a href='/booktest/index/'>跳到首页</a>")
    temp3 = loader.get_template("booktest/detail.html")
    book = BookInfo.objects.get(pk=id)
    result = temp3.render({"book": book})
    return HttpResponse(result)
def addbook(request):
    if request.method == "GET":
        return render(request, "booktest/addbook.html")
    elif request.method =="POST":
        title = request.POST.get("title")
        pub_date = request.POST.get("pub_date")
        book = BookInfo()
        book.title=title
        book.pub_date=pub_date
        book.save()
        return redirect(reverse("booktest:list"))

def deletebook(request,id):
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse("booktest:list"))

def addhero(request, id):
    book = BookInfo.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "booktest/addhero.html", {"book": book})
    elif request.method =="POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        gender = request.POST.get("gender")
        type = request.POST.get("type")
        hero = HeroInfo()
        hero.name = name
        hero.content = content
        hero.book = book
        hero.gender = gender
        hero.type = type
        hero.save()
        # return HttpResponse("添加成功")
        return redirect(reverse("booktest:detail", args=(id,)))
def deletehero(request,id):
    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    return redirect(reverse("booktest:detail", args=(bookid,)))