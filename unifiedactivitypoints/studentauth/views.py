from django.shortcuts import render,redirect
from .forms import UserForm

def signup(request):
    # print(request.POST)
    # if request.method == 'POST':
    #     form_contents = UserForm(request.POST)
    #     if form_contents.is_valid():
    #         form = form_contents.save()
    #         form.save()
    #         pass
    #     else:
    #         form = UserForm()
    return render(request,'studentauth/login.html')
