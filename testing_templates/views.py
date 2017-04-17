from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testing_templates/index.html')

def other(request):
    return render(request,'testing_templates/other.html')

def relative(request):
    return render(request,'testing_templates/relative_url_templates.html')
