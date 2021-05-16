"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from.forms import AnketaForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm
from orders.models import Order
from orders.models import OrderItem

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )
def users_orders(request):
    """Renders the about page."""
    #users_orders = Order.objects.filter(nickname=request.user)
    users_orders = Order.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/users_orders.html', {'users_orders': users_orders,}
    ) 


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Наши контакты.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Информация о нашей компании.',
            'year':datetime.now().year,
        }
    )
def links(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Ссылки',
            'message':'Наши партнеры.',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина', '2': 'Женщина'}
    internet = {'1': 'Каждый день', '2':'Несколько раз в день', 
               '3':'Несколько раз в неделю', '4':'Несколько раз в месяц'}
    if request.method == "POST":
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data ['gender']]
            data['internet'] = internet[form.cleaned_data ['internet']]
            if(form.cleaned_data['notice']== True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None

    else:
        form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            
            'form':form,
            'data':data,
            
            
           
        }
    )

def registration(request):
    """Рендер страницы регистрации"""
    if request.method == "POST": #после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False #запрет на вход в админ раздел
            reg_f.is_active = True #активный пользователь
            reg_f.date_joined = datetime.now() #дата регистрации
            reg_f.last_login = datetime.now() #дата последней авторизации

            regform.save() # сохраняем изменения после добавления полей
            return redirect('home') #переодресация на главную стр после регистрации
    else:
        regform = UserCreationForm() #создание объекта формы для ввода данных
    assert isinstance(request,HttpRequest)
    return render(request, 'app/registration.html', {'regform':regform, 'year':datetime.now().year,})

def blog(request):
    posts = Blog.objects.all() #запрос на выбор всех статей из модели
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Полезные статьи',
            'posts':posts,
            'year':datetime.now().year,
        }
    )


def blogpost(request,parametr):
    post_1 = Blog.objects.get(id=parametr) #запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST": #после отправки данных формы на сервер мтеодом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            
            return redirect('blogpost', parametr=post_1.id) #переадресация на ту же стр
    else:
         form=CommentForm() #создание формы для ввода комментария

        
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            
            'post_1':post_1, #передача конкретной статьи в шаблон веб стр
            'comments':comments,
            'form':form,
            'year':datetime.now().year,
        }
    )

def newpost(request):
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()

            blog_f.save() #сохранение изменения после добавления

            return redirect('blog')
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render (
        request,
        'app/newpost.html',
        {
            'blogform':blogform,
            'year': datetime.now().year
            }
        )


def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'О нас',
            'message':'Информация о нашей компании.',
            'year':datetime.now().year,
        }
    )


