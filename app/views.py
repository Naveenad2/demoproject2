from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def main_page(request):
     
     if request.user.id != None:
          
         user =  User.objects.get(id=request.user.id)

     else:
         user = None

     home_page_details = Edit_Home_Page.objects.all()
          
     return render(request,'main.html',{"user":user,"details":home_page_details})

def Login(request):
      
      if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)


        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,"wrongPass.html")
      return render(request,'login.html')

def Register(request):

     if request.method == "POST":

            name = request.POST.get('name')    
            email = request.POST.get('email')  
            pas = request.POST.get('pass')     
            repass = request.POST.get('repass')

            if pas == repass:

                    user = User.objects.filter(username=name)
                    isuser = user.exists()
                    if isuser is False:
                        new_user = User.objects.create_user(username=name,email=email,password=pas)
                        new_user.save()

                        authuser = authenticate(username=name,password=pas)
                        login(request,authuser)
                        return redirect('/')
            else:
                    return HttpResponse("password Does not match ")  
     else:
         return render(request,"register.html")


def lectures_cat(request):
                
     all_category =  Lecture_category.objects.all()
     return render(request,'lectures_cat.html',{"detailss":all_category})

def get_video(request,id):
     
     data = Lecture_category.objects.get(id=id)

     Video_data = Video.objects.filter(Choose_catogory=data)
     
     return render(request,'all_video_page.html',{"v_data":Video_data})

def play_video(request,id):
     
     get_video = Video.objects.get(id=id)

     return render(request,'main_video.html',{"l_video":get_video})

def Logout_(request):
       logout(request)
       return redirect("/login")