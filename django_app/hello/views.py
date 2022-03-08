from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import QuerySet
from django.views.generic import ListView, DetailView
from .models import Friend
from .forms import HelloForm
from .forms import FriendForm


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


def index(request):
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
