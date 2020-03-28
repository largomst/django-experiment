from django.shortcuts import render, redirect
from .forms import PropertyForm

# Create your views here.


items = "1 2 3 4 5".split(" ")


def index(request):
    if request.method == "POST":
        item = request.POST.get("property")
        if item:
            items.remove(item)
            redirect("index")
        else:
            items.append(request.POST.get("add"))

    template_name = "index.html"
    return render(request, template_name, {"items": items})


data = [{"1": 1, "2": 2}, {"2": 2, "3": 3}]


def table(request):
    template_name = "table.html"
    return render(request, template_name, {"heads": items, "data": data})
