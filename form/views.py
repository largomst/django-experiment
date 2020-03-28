from django.shortcuts import render,redirect

# Create your views here.


def index(request):
    if request.method == 'POST':
        property = request.POST.get('property')
        print(property)
        redirect('index')
    else:
        pass

    template_name = "index.html"
    return render(request, template_name)
