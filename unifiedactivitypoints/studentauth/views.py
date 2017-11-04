from django.views import View
from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from .models import UserProfile

def signup(request):
    print(request.POST)
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form = form_contents.save()
            form.save()
        else:
            form = UserForm()

    return render(request,'studentauth/signup.html',{'form':form,})


class Login(View):
    form_class = LoginForm
    template_name = "studentauth/login.html"

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            name = form.cleaned_data['registration_no']
            pwd = form.cleaned_data['password']
            try:
                result = UserProfile.objects.get(registration_no=name,password=pwd )
                if result:
                    return redirect("success")

            except UserProfile.DoesNotExist:
                form = LoginForm()
                return render(request,self.template_name,{"form":form})


    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
