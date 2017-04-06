from django.conf.urls import url
from demoHelp import views

urlpatterns = [
 url(r'^$',views.help,name='demoHelp'), # demoHelp is the name of the view
]
