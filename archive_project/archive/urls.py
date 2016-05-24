from django.conf.urls import url
from archive import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
]
