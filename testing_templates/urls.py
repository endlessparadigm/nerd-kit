from django.conf.urls import url
from . import views

# template tagging
app_name = 'testing_templates'

urlpatterns=[ # this means if you go to /testing_templates/relative (or other) it will go to that page
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
