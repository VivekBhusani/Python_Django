from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def entry(request):

    return render(request,'home.html')

# Create your views here.
def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= UserCreationForm()
    return render(request,'register.html',{'form':form})



def login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()


    return render(request,'login.html',{'form':form})

def home(request):

    return render(request,'index.html')


