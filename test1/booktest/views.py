from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.http import HttpResponse
from django.template import loader
from .admin import BookInfo,HeroInfo
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