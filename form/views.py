from django.shortcuts import render, redirect
from .forms import PropertyForm

# Create your views here.


heads = "1 2 3 4 5".split(" ")


def index(request):
    if request.method == "POST":
        head = request.POST.get("property")
        if head:
            heads.remove(head)
            redirect("index")
        else:
            heads.append(request.POST.get("add"))

    template_name = "index.html"
    return render(request, template_name, {"heads": heads})


data = [{"1": 1, "2": 2}, {"2": 2, "3": 3}]


def table(request):
    template_name = "table.html"
    return render(request, template_name, {"heads": heads, "data": data})


def new_record(request):
    template_name = "new_record.html"

    if request.method == "POST":
        record = {}
        for head in heads:
            record.update({head: request.POST.get(str(head) + "_value")})
        data.append(record)
        return redirect("table")
    elif request.method == "GET":
        return render(request, template_name, {"heads": heads})
