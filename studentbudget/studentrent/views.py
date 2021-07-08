from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View




# Create your views here.

def index(request):
    rent = renthouse.objects.all()
    return render (request,'index.html',{"newhouse":rent})




 

def aboutus (request):
    return render (request,'aboutus.html')

def search (request):
   qur = request.GET.get('search').lower()
   housesearch =[item for item in renthouse.objects.all() if qur in item.housetype.lower() or qur in item.address.lower() ]
   return render (request,'search.html',{'housesearch':housesearch})

 

def renter_dashboard (request):
    rent = renthouse.objects.all()
    return render (request, 'renter_dashboard.html',{'newhouse':rent} ) 

def renter_search (request):

    qur =request.GET.get('renter_search').lower()
    #housesearch = renthouse.objects.filter(housetype__contains = qur)
    renter_housesearch =[item for item in renthouse.objects.all() if qur in item.housetype.lower() or qur in item.address.lower() ]
    return render (request,'renter_dashboard.html',{'renter_housesearch':renter_housesearch})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else: 
            messages.info(request,'invalid credentials')
            return redirect("login")

    else:
        return render (request, 'login.html')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exits')
                return redirect('signup')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already used')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect ('login')
        
        else:
            messages.info(request,'Password not matching!')
            return redirect('signup')
        return redirect('/')

    else:
        return render(request, 'signup.html')

 
def logout(request):
    auth.logout(request)
    return redirect('/')

#renter login
def renter_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('/')

        else: 
            messages.info(request,'invalid credentials')
            return redirect("renter_login")

    else:
        return render (request, 'renter_login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def renter_signup(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exits')
                return redirect('renter_signup')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already used')
                return redirect('renter_signup')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect ('renter_login')
        
        else:
            messages.info(request,'Password not matching!')
            return redirect('renter_signup')
        return redirect('/')

    else:
        return render(request, 'renter_signup.html')

#landlord login
def landlord_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('landlord_dashboard')

        else: 
            messages.info(request,'invalid credentials')
            return redirect("landlord_login")

    else:
        return render (request, 'landlord_login.html')

def landlord_signup(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exits')
                return redirect('landlord_signup')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already used')
                return redirect('landlord_signup')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect ('landlord_login')
        
        else:
            messages.info(request,'Password not matching!')
            return redirect('landlord_signup')
        return redirect('/')

    else:
        return render(request, 'landlord_signup.html')


class details(DetailView):
    context_object_name= 'obj'
    template_name = 'details.html'
    model = renthouse





class apply(DetailView):
    context_object_name= 'renhouseid'
    template_name = 'renter_payment.html'
    model = renthouse


 
def renter_payment(request):
    renthouseid =request.POST['renthouseid']
    renter_name = request.POST['renter_name']
    cardholder_name =request.POST['cardholder_name']
    cardnumber = request.POST['cardnumber']
    expiry_date = request.POST ['expiry_date']
    cvc= request.POST['cvc']
    email= request.POST['email']

    new_housebooking = housebooking(renthouseid=renthouseid, renter_name=renter_name,cardholder_name=cardholder_name,
     cardnumber=cardnumber,expiry_date=expiry_date,cvc=cvc,email=email )

    new_housebooking.save()
    messages.info(request, 'Your booking has been successfully completed!')
    return redirect('/')