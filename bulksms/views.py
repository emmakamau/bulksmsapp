from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.core.paginator import Paginator
import csv, datetime
from datetime import date
import pandas as pd
import africastalking



username = "tamkbulksms"
api_key = "55b428d334336120e75b0120b07991d3fa29498eeb3a708c94f2e05297a96430"
africastalking.initialize(username, api_key)
sms = africastalking.SMS


# Create your views here.

@login_required(login_url='login')
def home(request):

    context = {
    }
    return render (request, 'bulksms/index.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def registeruser(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {
        'form': form,
    }
    return render (request, 'bulksms/registeruser.html', context=context)

@login_required(login_url='login')
def logoutuser(request):

    context = {
    }
    logout(request)
    return render (request, 'bulksms/logout.html', context=context)

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'bulksms/loginuser.html', context=context)

@login_required(login_url='login')
def automarkstat(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = AutoMarkMessage.objects.filter(date__range=(fromdate,todate))
        
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=automark.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'description', 'date', 'msgcount', 'custcount', 'message'])
        searchresult = searchresult.values_list('id','description', 'date', 'msgcount', 'custcount', 'message')
        for searchresult in searchresult:
            writer.writerow(searchresult)
        return response
    else:
        texts = AutoMarkMessage.objects.all().order_by('-id')
        paginator = Paginator(texts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render (request, 'bulksms/automarkstat.html', context=context)

@login_required(login_url='login')
def autofaststat(request):

    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = AutoFastMessage.objects.filter(date__range=(fromdate,todate))
        
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=autofast.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'description', 'date', 'msgcount', 'custcount', 'message'])
        searchresult = searchresult.values_list('id','description', 'date', 'msgcount', 'custcount', 'message')
        for searchresult in searchresult:
            writer.writerow(searchresult)
        return response
    else:
        texts = AutoFastMessage.objects.all().order_by('-id')
        paginator = Paginator(texts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
    }
    return render (request, 'bulksms/autofaststat.html', context=context)

@login_required(login_url='login')
def winpartstat(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = WinPartsMessage.objects.filter(date__range=(fromdate,todate))
        
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=winpart.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'description', 'date', 'msgcount', 'custcount', 'message'])
        searchresult = searchresult.values_list('id','description', 'date', 'msgcount', 'custcount', 'message')
        for searchresult in searchresult:
            writer.writerow(searchresult)
        return response
    else:
        texts = WinPartsMessage.objects.all().order_by('-id')
        paginator = Paginator(texts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render (request, 'bulksms/winpartstat.html', context=context)

@login_required(login_url='login')
def autofasttotalstat(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = AutoFastTotal.objects.filter(date__range=(fromdate,todate))
        
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=totalautofast.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'description', 'date', 'msgcount', 'custcount', 'message'])
        searchresult = searchresult.values_list('id','description', 'date', 'msgcount', 'custcount', 'message')
        for searchresult in searchresult:
            writer.writerow(searchresult)
        return response
    else:
        texts = AutoFastTotal.objects.all().order_by('-id')
        paginator = Paginator(texts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render (request, 'bulksms/autofasttotalstat.html', context=context)


@login_required(login_url='login')
def corpsmsstat(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = CorpMessage.objects.filter(date__range=(fromdate,todate))
        
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=corpsms.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'description', 'date', 'msgcount', 'custcount', 'message'])
        searchresult = searchresult.values_list('id','description', 'date', 'msgcount', 'custcount', 'message')
        for searchresult in searchresult:
            writer.writerow(searchresult)
        return response
    else:
        texts = CorpMessage.objects.all().order_by('-id')
        paginator = Paginator(texts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render (request, 'bulksms/corpsmsstat.html', context=context)


@login_required(login_url='login')
def automarksms(request):
    texts = AutoMarkMessage.objects.all().order_by('-id')[:5]

    if request.method == 'GET':
        form = automarksmsForm()
    else:
        form = automarksmsForm(request.POST)
        if form.is_valid():
            customer_list = pd.read_excel(request.FILES.get('excel_file'))
            msg = form.cleaned_data.get('message')
            description = form.cleaned_data.get('description')
            
            optout = "OPTOUT *456*9*5#"
            
            message = msg + optout
            date = datetime.datetime.now()
            user = request.user

            recipients_list = customer_list['Numbers'].values
            msgcount = 0
            custcount = 0
            for numbers in recipients_list:
                recipients = []
                phone = "+" + str(numbers)
                recipients.append(phone)
                custcount = custcount + 1
                msglength = len(message)
                if msglength > 160:
                    msgcount = msgcount + 2
                else:
                    msgcount = msgcount + 1
                for phone in recipients:
                    response = sms.send(message, recipients)
                    print(msgcount, date, custcount)

            AutoMarkMessage.objects.create(
                message = message,
                description = description,
                date = date,
                msgcount = msgcount,
                custcount = custcount,
                user = user,
            )
            messages.info(request, "Messages sent successfully.")
            return redirect('home')

    context = {
        'form':form,
        'texts':texts,
    }
    return render (request, 'bulksms/automarksms.html', context=context)

@login_required(login_url='login')
def autofastsms(request):
    texts = AutoFastMessage.objects.all().order_by('-id')[:5]

    if request.method == 'GET':
        form = autofastsmsForm()
    else:
        form = autofastsmsForm(request.POST)
        if form.is_valid():
            customer_list = pd.read_excel(request.FILES.get('excel_file'))
            msg = form.cleaned_data.get('message')
            description = form.cleaned_data.get('description')
            
            optout = "OPTOUT *456*9*5#"
            
            message = msg + optout
            date = datetime.datetime.now()
            user = request.user

            recipients_list = customer_list['Numbers'].values
            msgcount = 0
            custcount = 0
            for numbers in recipients_list:
                recipients = []
                phone = "+" + str(numbers)
                recipients.append(phone)
                custcount = custcount + 1
                msglength = len(message)
                if msglength > 160:
                    msgcount = msgcount + 2
                else:
                    msgcount = msgcount + 1
                for phone in recipients:
                    response = sms.send(message, recipients)
                    print(date)

            AutoFastMessage.objects.create(
                message = message,
                description = description,
                date = date,
                custcount = custcount,
                msgcount = msgcount,
                user = user,
            )
            messages.info(request, "Messages sent successfully.")
            return redirect('home')

    context = {
        'form':form,
        'texts':texts,
    }
    return render (request, 'bulksms/autofastsms.html', context=context)

@login_required(login_url='login')
def winpartsms(request):
    texts = WinPartsMessage.objects.all().order_by('-id')[:5]

    if request.method == 'GET':
        form = winpartsmsForm()
    else:
        form = winpartsmsForm(request.POST)
        if form.is_valid():
            customer_list = pd.read_excel(request.FILES.get('excel_file'))
            msg = form.cleaned_data.get('message')
            description = form.cleaned_data.get('description')
            
            optout = "OPTOUT *456*9*5#"
            
            message = msg + optout
            date = datetime.datetime.now()
            user = request.user

            recipients_list = customer_list['Numbers'].values
            msgcount = 0
            custcount = 0
            for numbers in recipients_list:
                recipients = []
                phone = "+" + str(numbers)
                recipients.append(phone)
                custcount = custcount + 1
                msglength = len(message)
                if msglength > 160:
                    msgcount = msgcount + 2
                else:
                    msgcount = msgcount + 1
                for phone in recipients:
                    response = sms.send(message, recipients)
                    print(date)

            WinPartsMessage.objects.create(
                message = message,
                description = description,
                date = date,
                msgcount = msgcount,
                custcount = custcount,
                user = user,
            )
            messages.info(request, "Messages sent successfully.")
            return redirect('home')

    context = {
        'form':form,
        'texts':texts,
    }
    return render (request, 'bulksms/winpartsms.html', context=context)

@login_required(login_url='login')
def autofasttotal(request):
    texts = AutoFastTotal.objects.all().order_by('-id')[:5]

    if request.method == 'GET':
        form = autofasttotalForm()
    else:
        form = autofasttotalForm(request.POST)
        if form.is_valid():
            customer_list = pd.read_excel(request.FILES.get('excel_file'))
            msg = form.cleaned_data.get('message')
            description = form.cleaned_data.get('description')
            
            optout = "OPTOUT *456*9*5#"
            
            message = msg + optout
            date = datetime.datetime.now()
            user = request.user

            recipients_list = customer_list['Numbers'].values
            msgcount = 0
            custcount = 0
            for numbers in recipients_list:
                recipients = []
                phone = "+" + str(numbers)
                recipients.append(phone)
                custcount = custcount + 1
                msglength = len(message)
                if msglength > 160:
                    msgcount = msgcount + 2
                else:
                    msgcount = msgcount + 1
                for phone in recipients:
                    response = sms.send(message, recipients)
                    print(date)

            AutoFastTotal.objects.create(
                message = message,
                description = description,
                date = date,
                custcount = custcount,
                msgcount = msgcount,
                user = user,
            )
            messages.info(request, "Messages sent successfully.")
            return redirect('home')

    context = {
        'form':form,
        'texts':texts,
    }
    return render (request, 'bulksms/autofasttotal.html', context=context)


@login_required(login_url='login')
def corpsms(request):
    texts = CorpMessage.objects.all().order_by('-id')[:5]

    if request.method == 'GET':
        form = corpsmsForm()
    else:
        form = corpsmsForm(request.POST)
        if form.is_valid():
            customer_list = pd.read_excel(request.FILES.get('excel_file'))
            msg = form.cleaned_data.get('message')
            description = form.cleaned_data.get('description')
            
            optout = "OPTOUT *456*9*5#"
            
            message = msg + optout
            date = datetime.datetime.now()
            user = request.user

            recipients_list = customer_list['Numbers'].values
            msgcount = 0
            custcount = 0
            for numbers in recipients_list:
                recipients = []
                phone = "+" + str(numbers)
                recipients.append(phone)
                custcount = custcount + 1
                msglength = len(message)
                if msglength > 160:
                    msgcount = msgcount + 2
                else:
                    msgcount = msgcount + 1
                for phone in recipients:
                    response = sms.send(message, recipients)
                    print(date)

            CorpMessage.objects.create(
                message = message,
                description = description,
                date = date,
                custcount = custcount,
                msgcount = msgcount,
                user = user,
            )
            messages.info(request, "Messages sent successfully.")
            return redirect('home')

    context = {
        'form':form,
        'texts':texts,
    }
    return render (request, 'bulksms/corpsms.html', context=context)


