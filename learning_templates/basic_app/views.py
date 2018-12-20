from django.shortcuts import render

def index(request):
    filterList = {'text':'this website was made using Django framework', 'number':100}
    return render(request, 'basic_app/index.html', filterList)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative.html')
