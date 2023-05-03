from django.shortcuts import render ,  redirect
# from datetime import datetime
from home.models import contact
from django.contrib.auth import login, authenticate, logout
# from home.models import users
from home.models import Details
from django.core import serializers 
# from .forms import SignupForm
from django.contrib import messages
from django.http import HttpResponse    
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError





@login_required
def HomePage(request):
    return render(request, 'index.html', {})



@login_required
def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)



    # Create your views here.
def index(request):
    return render(request,'index.html',)
    #return HttpResponse("This is homepage")
def about(request): 
    return render(request,'about.html',)
    #return HttpResponse("This is aboutpage")
@login_required
def services(request):
    ins=Details()   
    data = serializers.serialize('python',Details.objects.all())
    context = {
        'data':data,
    }
    print(context)
    return render(request,'services.html',context)
    #return HttpResponse("This is Servicespage")
@login_required
def cont(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=contact()
        ins.name=name
        ins.email=email
        ins.message=message
        ins.save()
    return render(request,'contact.html',)  
    # return HttpResponse("This is contactpage")
@login_required
def admine(request):
    if request.method == "POST":
        name= request.POST.get('name', False);
        cus_id= request.POST.get('cus_id', False);
        bill= request.POST.get('bill', False);
        ins=Details()
        ins.name=name
        ins.cus_id=cus_id
        ins.bill=bill
        ins.save()                                                                                      
    return render(request,'admine.html',)

#register
def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # Validate the input data
        if not all([fname, lname, name, email, password]):
            messages.error(request, "Please fill in all required fields")
            return redirect('register-page')

        try:
            new_user = User.objects.create_user(username=name, email=email, password=password)
            new_user.first_name = fname
            new_user.last_name = lname
            new_user.save()
        except IntegrityError:
            messages.error(request, "Username or email already taken")
            return redirect('register-page')

        messages.success(request, "Registration successful, you can now log in")
        return redirect('login-page')
   
  
    return render(request, 'signup.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home1.html', {})
        else:
            error_message = ''
            try:
                user = User.objects.get(username=name)
                error_message = 'Wrong password'
            except User.DoesNotExist:
                error_message = 'Error, user does not exist'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html', {})



def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'test.html', {})
