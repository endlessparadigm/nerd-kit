from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): # request can be any word
#   return HttpResponse("Hello World!")# works.
    my_dictionary = {'insert_me':"Hello I am from views.py!"}
    return render(request,'appHelloWorld/index.html',context=my_dictionary)

def help(request): # request can be any word
#   return HttpResponse("Hello World!")# works.
    help_dict = {'help_insert':"HELP PAGE"}
    return render(request,'demoHelp/help.html',context=help_dict)
