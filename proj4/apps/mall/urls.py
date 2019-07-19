from django.conf.urls import url
from . import views
app_name = "mall"
urlpatterns = [
    url('^$', views.index, name="index"),
    url(r'^list/$', views.ListView.as_view(), name='list'),
    url(r'^simple/(\d+)/$', views.SimpleView.as_view(), name="simple"),
    url(r'^cart/$', views.CartView.as_view(), name="cart"),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^account/$', views.AccountView.as_view(), name="account"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    # url(r'^register/$', views.register, name="register"),
]