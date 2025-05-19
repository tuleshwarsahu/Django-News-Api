from django.shortcuts import render , redirect
from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .utils import *

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        initial_data = { 'username': '', 'password1': '', 'password2': '' }
        form = UserCreationForm(initial=initial_data)
    return render(request, 'register.html' , {'form': form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm (request , data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        
    else:
        initial_data = { 'username': '', 'password1': '' }
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html' , {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
    # return render(request, 'logout.html')

@auth
def dashboard(request):
    return render(request, 'dashboard.html')




def home(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2025-04-19&sortBy=publishedAt&apiKey=15d89ffcb9e04883889397fdc8f2ee98'
    get_news_from_api(url)
    return render(request, 'home.html', context = {'articles': Articles.objects.all()})