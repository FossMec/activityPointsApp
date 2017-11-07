from django.conf.urls import url
from core import views

urlpatterns =[
    url('^$',views.home,name="home"),
]
