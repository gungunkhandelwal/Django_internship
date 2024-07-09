from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from . forms import *
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'loginView.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'loginView.html')

def signup(request):
    if request.method =='POST':
        form=UserSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            print("save successfuly")
            login(request,user)
            return redirect('dashboard')
    else:
        form=UserSignUpForm()
    
    return render(request,'signup.html',{'form':form})

def dashboard(request):
    if request.user.is_patient:
        return render(request,'dashboard_patient.html')
    elif request.user.is_doctor:
        return render(request,'dashboard_doctor.html')
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))