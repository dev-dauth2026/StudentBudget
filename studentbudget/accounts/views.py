from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
def index(request):
    return render (request,'index.html')
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
            return render (request, 'renter_dashboard.html')

        else: 
            messages.info(request,'invalid credentials')
            return redirect("renter_login")

    else:
        return render (request, 'renter_login.html')

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


def details(request):
   
    return render(request,'details.html')