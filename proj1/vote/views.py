from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice
# Create your views here.
def checklogin(fun):
    def check(request, *args):
        # username = request.COOKIES.get("username")
        username = request.session.get("username")
        if username:
            return fun(request, *args)
        else:
            return redirect(reverse("vote:login"))
    return check
@checklogin
def index(request):
    # username = request.COOKIES.get("username")
    username = request.session.get("username")
    # if username:
    questions = Question.objects.all()
    return render(request, "vote/index.html", locals())
    # else:
    #     return redirect(reverse("vote:login"))
@checklogin
def detail(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return HttpResponse("id非法")
    except Question.MultipleObjectsReturned:
        return HttpResponse("id非法")
    if request.method == "GET":
        return render(request, "vote/detail.html", locals())
    elif request.method == "POST":
        choiceid = request.POST.get("choice")
        choice = Choice.objects.get(pk=choiceid)
        choice.votes += 1
        choice.save()
        # Choice.objects.incresevotes(choiceid)
        # 没有重定向，刷新浏览器会再次发起post请求，结果出错
        # return render(request, "vote/result.html", {"question":question})
        return redirect(reverse("vote:result", args=(id,)))
@checklogin
def result(request, id):
    # question = Question.objects.get(pk=id)
    question = get_object_or_404(Question, pk=id)
    return render(request, "vote/result.html", locals())
def login(request):
    if request.method == 'GET':
        return render(request, "vote/login.html")
    elif request.method == 'POST':
        # 检测用户名密码是否对应
        # 1.登录成功需要存储cookie
        # response = redirect(reverse("vote:index"))
        # response.set_cookie("username", request.POST.get("username"))
        # return response
        # 2.使用session存储信息
        request.session["username"] = request.POST.get("username")
        return redirect(reverse("vote:index"))
def logout(request):
    # result = redirect(reverse("vote:login"))
    # result.delete_cookie("username")
    # return result
    request.session.flush()
    return redirect(reverse("vote:login"))