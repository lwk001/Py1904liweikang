from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator, Page
# Create your views here.
class IndexView(View):
    def get(self, request):
        # return HttpResponse('首页')
        ads = Ads.objects.all()
        articles = Article.objects.all()
        pagenum = request.GET.get("page")
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles, 1).get_page(pagenum)

        return render(request, 'blog/index.html', locals())
class SingleView(View):
    def get(self, request, id):
        article = get_object_or_404(Article, pk=id)
        article.views += 1
        article.save()
        cf = CommentForm
        # return HttpResponse('详情页')
        return render(request, 'blog/single.html', {"article": article, "cf": cf})
    def post(self, request,id):
        # return HttpResponse('评论成功')
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(reverse('blog:single', args=(article.id,)))
class AddArticleView(View):
    def get(self, request):
        af = ArticleForm()
        return render(request, 'blog/addarticle.html', locals())
    def post(self, request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))

        return HttpResponse("添加失败")
