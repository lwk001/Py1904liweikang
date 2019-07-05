
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.http import HttpResponse
from . import views

app_name = 'booktest'

# #自定义视图函数 绑定路由
# def myview(request):
#     return HttpResponse("自定义路由展示页面")
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    ]
