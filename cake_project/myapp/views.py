from django.shortcuts import render
from .models import *

from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def index(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])

        context = {
            'uid' : uid
        }

        return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")#6



def login(request):

    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])

        context = {
            'uid' : uid
        }

        return render(request,"myapp/index.html",context)
    else:
        try:
            if request.POST:
                email = request.POST['email']
                password = request.POST['password']

                uid = User.objects.get(email=email)

                if uid.password == password:


                    request.session['email'] = uid.email

                    context = {
                        'uid' : uid
                    }
                    return render(request,"myapp/index.html",context)
                else:
                    context = {

                        'p_msg' : "INVALID PASSWORD......."
                    }
                    return render(request,"myapp/login.html",context)
            else:
                return render(request,"myapp/login.html")
        except:
            context = {
                'e_msg' : "Invalid Email......"
            }
            return render(request,"myapp/login.html",context)


def logout(request):
    if "email" in request.session:

        del request.session['email']

        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")



def registration(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        contact = request.POST['contact']
        address = request.POST['address']

        uid = User.objects.create(email = email,
                                  password=password,
                                  username=username,
                                  f_name=f_name,
                                  l_name=l_name,
                                  contact=contact,
                                  address=address,
                                  )
        context = {
            'uid' : uid,
            'r_msg' : "Successefully Register....."
        }
        return render(request,"myapp/login.html",context)
    else:
        return render(request,"myapp/registration.html")





def about(request):
    return render(request,"myapp/about.html")


def contact(request):

    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        message = request.POST['message']

        uid = Contact.objects.create(name=name,
                                     email=email,
                                     subject=subject,
                                     message=message)
        context = {
            'uid' : uid
        }
        return render(request,"myapp/contact.html",context)
    else:
        return render(request,"myapp/contact.html")


def forget_password(request):

    if request.POST:
        email = request.POST['email']
        otp =  random.randint(1111,9999)
        
        try:

            uid = User.objects.get(email=email)

            if uid.email == email:
                uid.otp = otp
                uid.save()

                send_mail("forgot password","your otp is "+str(otp),"gohiljayb10@gmail.com",[email])
                
                context = {
                    'email' : email
                }
                return render(request,"myapp/comfrom_password.html",context)
            else:
                context = {
                    'e_msg' : "invalid email...."
                }
                return render(request,"myapp/forget_password.html",context)
        except:

            context = {
                    'e_msg' : "invalid email...."
            }
            return render(request,"myapp/forget_password.html",context)



    else:
        return render(request,"myapp/forget_password.html")



def confrom_password(request):

    if request.POST:
        otp =request.POST['otp']
        email = request.POST['email']
        new_password = request.POST['new_password']
        confrom_password = request.POST["confrom_password"]

        uid = User.objects.get(email=email)

        if str(otp) == otp:
            if new_password == confrom_password:
                uid.password = new_password
                uid.save()

                context = {
                    'email' : email
                }
                return render(request,"myapp/login.html",context)
            else:
                context = {
                    'p_msg' : "invalid password...."
                }
                return render(request,"myapp/comfrom_password.html",context)
        else:
                context = {
                    'o_msg' : "invalid OTP...."
                }
                return render(request,"myapp/comfrom_password.html",context)
    else:
        return render(request,"myapp/comfrom_password.html")







def product(request):
    return render(request,"myapp/product.html")
def service(request):
    return render(request,"myapp/service.html")
def team(request):
    return render(request,"myapp/team.html")
def testimonial(request):
    return render(request,"myapp/testimonial.html")
def err(request):
    return render(request,"myapp/err.html")
