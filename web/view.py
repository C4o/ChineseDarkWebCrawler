from django.http import HttpResponseRedirect
from django.shortcuts import render
from DrakWeb.models import *
from django.contrib.auth.hashers import make_password, check_password
import time
import random
import os

#index page
def index(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            return render(request, 'pages/index.html')
        else:
            return HttpResponseRedirect('/login/')

# login regist and logout
def regist(request):
    if request.method == 'GET':
        return render(request, 'pages/regist.html')
    if request.method == 'POST':
        print request.method
        # regist
        name = request.POST.get('username')
        password = request.POST.get('password')
        if name and password:
            # crypto the password
            password = make_password(password)
            User.objects.create(Username=name, Password=password)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/regist/')

def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    if request.method == 'POST':
        # if login success set cookie
        name = request.POST.get('username')
        password = request.POST.get('password')
        if name and password:
            # check if user exist
            if User.objects.filter(Username=name).exists():
                user = User.objects.get(Username=name)
                if check_password(password, user.Password):
                    # ticket = 'agdoajbfjad'
                    ticket = ''
                    for i in range(15):
                        s = 'abcdefghijklmnopqrstuvwxyz'
                        # get random string
                        ticket += random.choice(s)
                    now_time = int(time.time())
                    ticket = 'TK' + ticket + str(now_time)
                    # bind cookie with token
                    # response = HttpResponse()
                    response = HttpResponseRedirect('/index/')
                    #  cookie live time
                    response.set_cookie('ticket', ticket, max_age=10000)
                    # keep cookie in server
                    user.ticket = ticket
                    user.save()
                    return response
                else:
                    # return HttpResponse('username or password error')
                    return render(request, 'pages/login.html', {'password': 'username or password error'})
            else:
                # return HttpResponse('username or password error')
                return render(request, 'pages/login.html', {'name': 'username or password error'})
        else:
            return HttpResponseRedirect('/login/')

def logout(request):
    if request.method == 'GET':
        # response = HttpResponse()
        response = HttpResponseRedirect('/login/')
        response.delete_cookie('ticket')
        return response

#load data of Basic info of DrakWeb
def Read_Basic(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Basic.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Data(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Data.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Teach(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Teach.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Sex(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Sex.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_CVV(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = CVV.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Private(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Private.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Virtual_Source(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Virtual_Source.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Material(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Material.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Service(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Service.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')

def Read_Other(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        elif User.objects.filter(ticket=ticket).exists():
            rows = Other.objects.all().order_by('-Topic_post_time')
            try:
                for row1 in rows:
                    row = row1
                    break
                return render(request, 'pages/tables_common.html', {'rows':rows,'ct':row})
            except:
                return render(request, 'pages/tables_common.html', {'rows':rows})
        else:
            return HttpResponseRedirect('/login/')
