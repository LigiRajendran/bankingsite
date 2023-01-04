from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from . forms import Applicationform
from .models import  Applicationform



# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class IndexView(TemplateView):
        template_name = 'index.html'

def registration(request):
     if request.method == 'POST':
        username = request.POST['username']

        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repass']

        if password==repassword:

          if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exist")
            print("Username already exist")
            return redirect('/registration')
          elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exist")
            print("Email already exist")
            return redirect('/registration')
          else :
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.info(request, "Registration  completed ")
            print("User created")
            return redirect('/login')
        else:
            print("password not matching")
            messages.info(request,"password not matching")
            return redirect('/registration')
     return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            messages.info(request,"Invalid credential")

            return redirect('/login')
    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def application(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        phn = request.POST['phn']
        gender = request.POST['gender']
        account = request.POST['account']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        branch = request.POST['branch']
        materials = request.POST['materials']
        application = Applicationform(name=name, email=email, dob=dob, phn=phn, gender=gender, account=account,
                                      address=address, state=state, district=district, branch=branch,
                                      materials=materials)
        application.save();

        messages.info(request, "Application Submitted")
        print("User created")
        return redirect('/application')


    return render(request, "applicationform.html")






