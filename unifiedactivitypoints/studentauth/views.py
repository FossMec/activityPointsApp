import bcrypt
from django.views import View
from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from .models import UserProfile

def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            salt = bcrypt.gensalt(14)
            passer = form.cleaned_data['password']
            hash_pass = bcrypt.hashpw(passer.encode('utf-8'),salt)
            a.password = hash_pass
            a.save()
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
            # salt = bcrypt.gensalt(14)
            # hash_pass = bcrypt.hashpw(b'pwd',salt)
            
            try:
                result = UserProfile.objects.get(registration_no=name)
                if pwd == result.password:
                # if bcrypt.hashpw(hash_pass.encode('utf-8'),str(result.password)) == str(result.password):
                    request.session['member_id'] = result.id
                    return redirect("home")

            except UserProfile.DoesNotExist:
                form = LoginForm()
                return render(request,self.template_name,{"form":form})


    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})



class Success(View):
    template_name = "studentauth/success.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
