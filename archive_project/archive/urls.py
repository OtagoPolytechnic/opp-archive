from django.conf.urls import url
from archive import views
from forms import SearchForm

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'results/$', views.results, name='results'),
     url(r'details/$', views.details, name='details'),
     url(r'confirmation/$', views.confirmation, name='confirmation'),
]
