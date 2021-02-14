from django.shortcuts import render
from django.http import HttpResponse
from main.models import ToDoList, Item


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})

    # return render(response, "main/base.html", {"ls":ls})

    #item = ls.item_set.get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, item.text))

def home(response):
    return render(response, "main/home.html", {})