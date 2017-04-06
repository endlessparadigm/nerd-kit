from django.shortcuts import render
from users.models import User
# Create your views here.
def index(request):
    return render(request,'users/index.html')

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users':user_list}
    return render(request,'users/users.html',context=user_dict)
