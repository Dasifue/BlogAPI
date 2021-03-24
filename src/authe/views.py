from django.shortcuts import render, redirect
from django.http import JsonResponse
from authe.models import Author, ConfirmCode
from rest_framework.response import Response
from authe.forms import Register, LoginForm
from .utils import send_code_mail
from django.conf import settings
from main.settings import ALLOWED_HOSTS
from django.contrib.auth import authenticate 
from django.contrib.auth import  login as auth_login
from django.contrib.auth import logout

# Create your views here.

# def register(request):
#     form = Register()
#     author = Author.objects.all()
#     if request.method == 'POST':
#         save_form = Register(request.POST)
#         if save_form.is_valid():
#             if Author.objects.filter(username = username, verfied=True) or Author.objects.filter(email=email, verified=True):
#                 message = 'пользователь с таким именем или мейлом существует'
#                 return render(request, 'reply.html', {'message':message})
#             author = Author(username = request.POST['username'], email = request.POST['email'])
#             author.set_password(request.POST['password'])
#             author.save()
#             code = ConfirmCode.objects.create(author = author)
#             print(send_code_mail(author.email, code.code))
#         print(request.POST)
#     return render(request, 'register.html', {'form':form, 'author':author})

def register(request):
    form=Register()
    if request.method=='POST':
        save_form=Register(request.POST)
        if save_form.is_valid():
            author=Author(username=request.POST['username'],email=request.POST['email'])
            author.set_password(request.POST['password'])
            author.save()
            code= ConfirmCode.objects.create(author=author)
            send_code_mail(author.email,code.code)
            message = "Все ок"
            return render(request,'reply.html',{"message":message}) 
        elif Author.objects.filter(username = request.POST['username'], verified=False) or Author.objects.filter(email=request.POST['email'], verified=False):
            author = None
            if Author.objects.filter(email = request.POST['email']): 
                author = Author.objects.get(email = request.POST['email'])
            elif Author.objects.filter(username = request.POST['username']): 
                author = Author.objects.get(username = request.POST['username'])
            code= ConfirmCode.objects.create(author=author)
            send_code_mail(author.email,code.code)
            message = "Все ок" 
            return render(request, 'reply.html', {'message':message})    
        message=save_form.errors
        return render(request,'reply.html',{"message":message})    
                
    return render(request,'register.html',{'form':form})    


def confirm_email(request, code):
    code = ConfirmCode.objects.filter(code = code)
    message = 'ваш код не действителен'
    if code:
        if not code.last().confirm:
            code = code.last()
            code.confirm = True
            code.save()
            author = code.author
            author.verified = True
            author.save()
            message = 'ваша почта подтверждена'
    return render(request, 'reply.html', {'message':message})



def login(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            auth_login(request, user)
            return render(request, 'reply.html', {'message':'you signed in', 'success':True})
        return render(request, 'reply.html', {'message':'такой пользователь уже существует', 'success':False})
    return render(request, 'log_in.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('api:all_posts')