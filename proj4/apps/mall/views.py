from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import *

# Create your views here.
class IndexView(View):
    def get(self, request):
        ads = Ads.objects.all()
        return render(request, 'mall/index.html', locals())
class SimpleView(View):
    def get(self, request, id):
        products = Product.objects.all()
        return render(request, 'mall/simple-product.html')
    def post(self, request, id):
        return render(request, 'mall/simple-product.html')
class ListView(View):
    def get(self, request):
        products = Product.objects.all()
        categorys = Category.objects.all()
        return render(request, 'mall/list-view.html', locals())
