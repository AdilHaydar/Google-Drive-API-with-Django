from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import RegisterForm, LoginForm, UserUpdateForm
from .models import User
#from django.contrib.auth.models import User
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model()
def register(request):
    form = RegisterForm(request.POST or None)
    context = {
            "form" : form
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        cep_telefonu = form.cleaned_data.get("cep_telefonu")

        registeredUser = User(username = username,cep_telefonu=cep_telefonu, email = email,full_name=full_name,)
        registeredUser.set_password(password)
        registeredUser.save()
        login(request, registeredUser)

        messages.success(request,"Succussfull.")
        return redirect("index")

    return render(request,"register.html",context)
        
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,"User does not exist.")
            return render(request,"login.html",context)
        messages.success(request,"Giriş Başarılı")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Güvenli Bir Şekilde Çıkış Yaptınız")
    return redirect("index")




        
