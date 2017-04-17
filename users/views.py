from django.shortcuts import render
#from django.http import HttpResponse
from users.models import User
# Create your views here.
def index(request):
    return render(request,'users/index.html')

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form  invalid')
    return render(request,'users/users.html',{'form':form})





    #user_list = User.objects.order_by('last_name')
    #user_dict = {'users':user_list}
    #return render(request,'users/users.html',context=user_dict)
