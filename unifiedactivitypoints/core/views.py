from django.shortcuts import render
from django.views import View
from studentauth.models import UserProfile

# Create your views here.

def home(request):

    
    no_views = request.session.get('no_views',0)
    request.session['no_views'] = no_views+1
    return render(request,'core/dashboard.html',
        context={'viewcount':no_views,}
        )
