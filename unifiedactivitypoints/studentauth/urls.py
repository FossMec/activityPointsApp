from django.conf.urls import url
from studentauth import views

urlpatterns = [
url(r'^signup$',views.signup,name="signuppage"),
]
