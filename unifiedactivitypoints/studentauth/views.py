from django.shortcuts import render,redirect
from .forms import UserForm

def signup(request):
    print(request.POST)
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form = form_contents.save()
            form.save()
        else:
            form = UserForm()

    return render(request,'studentauth/signup.html',{'form':form,})
