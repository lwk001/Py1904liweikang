
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.http import HttpResponse
from . import views

# #自定义视图函数 绑定路由
# def myview(request):
#     return HttpResponse("自定义路由展示页面")
urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/$', views.list),
    url(r'^detail/(\d+)/$', views.detail),
    ]