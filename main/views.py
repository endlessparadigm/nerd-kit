from django.shortcuts import render
from django.http import HttpResponse
from main.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request): # request can be any word
#   return HttpResponse("Hello World!")# works.
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'main/index.html',context=date_dict)

    #my_dictionary = {'insert_me':"Hello I am from views.py!"}
    #return render(request,'appHelloWorld/index.html',context=my_dictionary)
