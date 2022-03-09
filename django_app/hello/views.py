from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import QuerySet
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count, Avg, Sum, Min, Max
from django.core.paginator import Paginator
from .models import Friend, Message
from .forms import FindForm, HelloForm
from .forms import FriendForm, MessageForm
from .forms import CheckForm


def message(request, page=1):
    if request.method == "POST":
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    # 新しいものから表示したい
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        "title": "Message",
        "form": MessageForm(),
        "data": paginator.get_page(page),
    }
    return render(request, "hello/message.html", params)


def index(request, num=1):
    """表示する項目を3つずつに分けて表示"""
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        "title": "Hello",
        "message": "",
        "data": page.get_page(num),
    }
    return render(request, "hello/index.html", params)


def check(request):
    params = {
        "title": "Hello",
        "message": "check validation",
        "form": FriendForm(),
    }
    if request.method == "POST":
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params["form"] = form
        if form.is_valid():
            params["message"] = "OK"
        else:
            params["message"] = "no good"
    return render(request, "hello/check.html", params)


def check_v1(request):
    params = {
        "title": "Hello",
        "message": "check validation",
        "form": CheckForm(),
    }
    if request.method == "POST":
        form = CheckForm(request.POST)
        params["form"] = form
        if form.is_valid():
            params["message"] = "OK"
        else:
            params["message"] = "no good."
    return render(request, "hello/check.html", params)


def find(request):
    if request.method == "POST":
        msg = request.POST["find"]
        form = FindForm(request.POST)
        sql = "select * from hello_friend"
        if msg != "":
            sql += " where " + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = "search words..."
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title": "Hello",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "hello/find.html", params)


def index_v12(request):
    data = Friend.objects.all()
    re1 = Friend.objects.aggregate(Count("age"))
    re2 = Friend.objects.aggregate(Sum("age"))
    re3 = Friend.objects.aggregate(Avg("age"))
    re4 = Friend.objects.aggregate(Min("age"))
    re5 = Friend.objects.aggregate(Max("age"))
    msg = (
        "Count:"
        + str(re1["age__count"])
        + "<br>Sum:"
        + str(re2["age__sum"])
        + "<br>Average:"
        + str(re3["age__avg"])
        + "<br>Min:"
        + str(re4["age__min"])
        + "<br>Max"
        + str(re5["age__max"])
    )
    params = {
        "title": "Hello",
        "message": msg,
        "data": data,
    }
    return render(request, "hello/index.html", params)


def find_v3(request):
    """範囲検索"""
    if request.method == "POST":
        msg = "search result:"
        form = FindForm(request.POST)
        find = request.POST["find"]
        lst = find.split()
        data = Friend.objects.all()[int(lst[0]) : int(lst[1])]
    else:
        msg = "search words..."
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title": "Hello",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "hello/find.html", params)


def index_v11(request):
    data = Friend.objects.all().order_by("age").reverse()
    params = {
        "title": "Hello",
        "message": "",
        "data": data,
    }
    return render(request, "hello/index.html", params)


def find_v2(request):
    """複数項目に対して同じキーワードで検索"""
    if request.method == "POST":
        msg = "search result:"
        form = FindForm(request.POST)
        find = request.POST["find"]
        data = Friend.objects.filter(Q(name__contains=find) | Q(mail__contains=find))
    else:
        msg = "search words..."
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title": "Hello",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "hello/find.html", params)


def find_v1(request):
    """単一検索"""
    if request.method == "POST":
        form = FindForm(request.POST)
        find = request.POST["find"]
        # *__containsで曖昧検索
        # *__startwithで接頭辞，*__endwithで接尾辞検索
        # *__iexactで大文字小文字を区別しない
        # *__icontains等もある
        # data = Friend.objects.filter(name__contains=find)
        # 数値の比較
        # lt, lte, gt, gteなどで大小比較
        data = Friend.objects.filter(age__lte=int(find))
        msg = f"Result: {data.count()}"
    else:
        msg = "search words..."
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title": "Hello",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "hello/find.html", params)


class FriendList(ListView):
    model = Friend


class FriendDeteil(DetailView):
    model = Friend


def delete(request, num):
    friend = Friend.objects.get(id=num)
    if request.method == "POST":
        friend.delete()
        return redirect(to="/hello")
    params = {
        "title": "Hello",
        "id": num,
        "obj": friend,
    }
    return render(request, "hello/delete.html", params)


def edit(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == "POST":
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/hello")
    params = {
        "title": "Hello",
        "id": num,
        "form": FriendForm(instance=obj),
    }
    return render(request, "hello/edit.html", params)


def index_v10(request):
    data = Friend.objects.all()
    params = {
        "title": "Hello",
        "data": data,
    }
    return render(request, "hello/index.html", params)


def create(request):
    """いちいちkeyを指定しないで登録する"""
    if request.method == "POST":
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/hello")
    params = {
        "title": "Hello",
        "form": FriendForm(),
    }
    return render(request, "hello/create.html", params)


# create model
def create_v1(request):
    params = {
        "title": "Hello",
        "form": HelloForm(),
    }
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        gender = "gender" in request.POST
        age = request.POST["age"]
        birth = request.POST["birthday"]
        # modelの作成
        friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth)
        friend.save()
        return redirect(to="/hello")
    return render(request, "hello/create.html", params)


def __new_str__(self):
    result = ""
    for item in self:
        result += "<tr>"
        for k in item:
            result += "<td>" + str(k) + "=" + str(item[k]) + "</td>"
        result += "</tr>"
    return result


# QuerySet.__str__ = __new_str__


def index_v9(request):
    data = Friend.objects.all().values("id", "name", "age")
    params = {
        "title": "Hello",
        "data": data,
    }
    return render(request, "hello/index.html", params)


def index_v8(request):
    num = Friend.objects.all().count()
    first = Friend.objects.all().first()
    last = Friend.objects.all().last()
    data = [num, first, last]
    params = {
        "title": "Hello",
        "data": data,
    }
    return render(request, "hello/index.html", params)


def index_v7(request):
    data = Friend.objects.all().values_list("id", "name")
    params = {
        "title": "Hello",
        "data": data,
    }
    return render(request, "hello/index.html", params)


def index_v6(request):
    params = {
        "title": "Hello",
        "message": "all friends",
        "form": HelloForm(),
        "data": [],
    }
    if request.method == "POST":
        num = request.POST["id"]
        item = Friend.objects.get(id=num)
        params["data"] = [item]
        params["form"] = HelloForm(request.POST)
    else:
        params["data"] = Friend.objects.all()
    return render(request, "hello/index.html", params)


def indexv5(request):
    data = Friend.objects.all()
    params = {
        "title": "Hello",
        "message": "all friends.",
        "data": data,
    }
    return render(request, "hello/index.html", params)


class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            "title": "Hello",
            "form": HelloForm(),
            "result": None,
        }

    def get(self, request):
        return render(request, "hello/index.html", self.params)

    def post(self, request):
        chk = request.POST["choice"]
        self.params["result"] = f"you selected {chk}."
        self.params["form"] = HelloForm(request.POST)
        return render(request, "hello/index.html", self.params)


def index_v4(request):
    params = {
        "title": "Hello",
        "message": "your data:",
        "form": HelloForm(),
    }
    if request.method == "POST":
        params["message"] = (
            "名前："
            + request.POST["name"]
            + "<br>メール："
            + request.POST["mail"]
            + "<br>年齢："
            + request.POST["age"]
        )
        params["form"] = HelloForm(request.POST)
    return render(request, "hello/index.html", params)


def index_v3(request):
    params = {
        "title": "Hello/Index",
        "msg": "What's your name?",
    }
    return render(request, "hello/index.html", params)


def form(request):
    msg = request.POST["msg"]
    params = {
        "title": "Hello/Form",
        "msg": f"hello, {msg}.",
    }
    return render(request, "hello/index.html", params)


def index_v2(request):
    params = {
        "title": "Hello/Index",
        "msg": "これはサンプルで作ったページです",
        "goto": "next",  # ここはurls.pyのname=...の値
    }
    return render(request, "hello/index.html", params)


def next(request):
    params = {
        "title": "Hello/Next",
        "msg": "これは，もう一つのページです",
        "goto": "index",
    }
    return render(request, "hello/index.html", params)


def index_v1(request, id, nickname):
    # if "msg" in request.GET:
    #     msg = request.GET["msg"]
    #     result = f"you typed: {msg}."
    # else:
    #     result = "please type msg parameter!"
    result = f"your id: {id}\n your nickname:'{nickname}'"
    return HttpResponse(result)
