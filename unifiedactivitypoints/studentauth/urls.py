from django.conf.urls import url
from studentauth import views

urlpatterns = [
url(r'^signup/$',views.signup,name="signuppage"),
url(r'^$',views.Login.as_view(),name="login"),
url(r'^succes/$',views.Success.as_view(),name='Success'),
]
