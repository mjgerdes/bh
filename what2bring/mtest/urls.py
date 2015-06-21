
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name_string>.+)/$', views.namestring, name='namestring')
]


