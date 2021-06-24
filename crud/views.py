from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserRegistrationForm
from .models import User

def home(request):
    form=UserRegistrationForm()
    data=User.objects.all()
    return render(request,'crud/home.html',{'form':form,'data':data})


def save_data(request):  
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            uid=request.POST.get('uid')
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            if uid:
                user=User(id=uid,name=name,email=email,password=password)
            else:    
                user=User(name=name,email=email,password=password)
            user.save()
            temp=User.objects.values()
            user_data=list(temp)
            return JsonResponse({"status":"save","user_data":user_data})

        else:
            return JsonResponse({"status":"failed"})
           
def delete_data(request):
    if request.method=="POST":
        id=request.POST.get("sid")
        obj=User.objects.get(pk=id)
        obj.delete()
        return JsonResponse({"status":"delete"})
    else:
        return JsonResponse({"status":"failed"})
def edit_data(request):
    if request.method=="POST":
        id=request.POST.get("sid")
        obj=User.objects.get(pk=id)
        user_data={"id":obj.id,"name":obj.name,"email":obj.email,"password":obj.password} 
        return JsonResponse(user_data)