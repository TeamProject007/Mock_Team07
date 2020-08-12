from django.shortcuts import render,redirect
from .forms import DonorForm,DoneeForm,ItemForm,RequirementForm
# Create your views here.
from .models import Item,Requirement
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'things/index.html')

@login_required
def special(request):
    return HttpResponse("Your logged in,Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def registerd(request):
    registered=False

    if request.method=='POST':
        user_form=DoneeForm(data=request.POST)


        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=DoneeForm()

    return render(request,'things/doneeform.html',{'user_form':user_form,'registered':registered})

def register(request):
    registered=False

    if request.method=='POST':
        profile_form=DonorForm(data=request.POST)


        if profile_form.is_valid():
            user=profile_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
        else:
            print(profile_form.errors)
    else:
        profile_form=DonorForm()

    return render(request,'things/donorform.html',{'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        doemail=request.POST.get('doemail')
        dopassword=request.POST.get('dopassword')


        user=authenticate(email=email,password=password)
        userd=authenticate(doemail=doemail,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        elif userd:
            if userd.is_active:
                login(request,userd)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username : {} and Password: {}".format(email,password))
            return HttpResponse("Invalid login details!")
    else:
        return render(request,'things/login.html',{})

def create_item(request):
    if request.method=='POST':
        form=ItemForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ItemForm()

    return render(request,'things/item-form.html',{'form':form})

def add_item(request):
    req_form=RequirementForm(request.POST or None)

    if req_form.is_valid():
        req_form.save()
        return redirect('things:index')

    return render(request,'things/requirement-form.html',{'req_form':req_form})

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'things/detail.html',context)

def detaild(request,req_id):
    req=Requirement.objects.get(pk=req_id)
    context={
        'req':req,
    }
    return render(request,'things/detaild.html',context)

def item(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'things/donors.html',context)

def req(request):
    req_list=Requirement.objects.all()
    context={
        'req_list':req_list,
    }
    return render(request,'things/donees.html',context)

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('things:index')

    return render(request,'things/item-need.html',{'item':item})

def delete_item2(request,id):
    req=Requirement.objects.get(id=id)
    if request.method=='POST':
        req.delete()
        return redirect('things:index')

    return render(request,'things/item-donate.html',{'req':req})
