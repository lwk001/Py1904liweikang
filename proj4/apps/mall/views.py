from django.shortcuts import render, get_object_or_404, reverse, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import CommentForm

# Create your views here.

def index(request):
    username = request.COOKIES.get("username")
    # if username:
    ads = Ads.objects.all()
    categorys = Category.objects.all()
    return render(request, 'mall/index.html', locals())

class IndexView(View):
    def get(self, request):
        username = request.COOKIES.get("username")
        ads = Ads.objects.all()
        categorys = Category.objects.all()
        return render(request, 'mall/index.html', locals())
class ListView(View):
    def get(self, request):
        username = request.COOKIES.get("username")
        products = Product.objects.all()
        categorys = Category.objects.all()
        return render(request, 'mall/list-view.html', locals())
class SimpleView(View):
    def get(self, request, id):
        username = request.COOKIES.get("username")
        # products = Product.objects.all()
        # products = get_list_or_404(Product, pk=id)
        product = get_object_or_404(Product, pk=id)
        product.views += 1
        product.save()
        cf = CommentForm()
        return render(request, 'mall/simple-product.html', locals())
    def post(self, request, id):
        product = get_object_or_404(Product, pk=id)
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.product = product
        comment.save()
        return redirect(reverse('mall:simple', args=(product.id,)))
class CartView(View):
    def get(self, request):
        username = request.COOKIES.get("username")
        products = Product.objects.all()
        return render(request, 'mall/cart.html', locals())
class AboutView(View):
    def get(self, request):
        username = request.COOKIES.get("username")
        return render(request, 'mall/about-us.html', locals())
class ContactView(View):
    def get(self, request):
        username = request.COOKIES.get("username")
        return render(request, 'mall/contact-us.html', locals())
class AccountView(View):
    def get(self, request):
        username = request.COOKIES.get("username")
        return render(request, 'mall/my.account.html', locals())
def login(request):
    if request.method == "GET":
        return render(request, 'mall/my.account.html')
    elif request.method == "POST":
        response = redirect(reverse("mall:index"))
        response.set_cookie("username", request.POST.get("username"))
        return response
def logout(request):
    response = redirect(reverse("mall:login"))
    response.delete_cookie("username")
    return response
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = mallUser.objects.create_user(username=username, password=password)
        if user:
            return redirect(reverse("mall:login"))
        else:
            return render(request, 'mall/my.account.html', {"errors": "注册失败"})
