from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate

# Create your views here.

def create(request):

    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        paswd = request.POST['password']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        gen = request.POST['gender']
        cntct = request.POST['contact']
        dob = request.POST['birthday']
        obj = CustomUser.objects.filter(email=email)
        if obj:
            messages.warning(request, "email already exists, please try again with different password")

            return HttpResponseRedirect(reverse('sign_up'))
        else:
            hashed_password = make_password(paswd)
            fm = CustomUser.objects.create(email=email, password=hashed_password,
                firstname=fname, lastname=lname, gender=gen,contact=cntct, dob=dob)
            fm.save()
    data = CustomUser.objects.all()
    context = {
        "data_info": data,
    }

    return render(request, 'sign_up.html', context)