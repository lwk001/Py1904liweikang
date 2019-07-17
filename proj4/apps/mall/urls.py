from django.conf.urls import url
from . import views
app_name = "mall"
urlpatterns = [
    url('^$', views.IndexView.as_view(), name="index"),
    url(r'^list/$', views.ListView.as_view(), name='list'),
    url('^simple/(\d+)/$', views.SimpleView.as_view(), name="simple"),

]