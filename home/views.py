from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from home.models import Food 
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def home(request):
    # Lấy dữ liệu từ cơ sở dữ liệu hoặc tạo ra một giá trị mẫu
    foods = Food.objects.filter(hotFood= True)
    
    # Đặt biến foods vào context
    context = {'foods': foods}

    # Trả về render với context
    return render(request, 'pages/home.html', context)


def menu(request):
    return render(request, 'pages/menu.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        user = authenticate(request, username= userName, password= passWord)
        if user is not None:
            login(request,user)
            return redirect('index')
        else: messages.info(request,'user or password not correct!')
            
    context={}
    return render(request, 'pages/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form' :form}
    return render(request, 'pages/register.html',context)