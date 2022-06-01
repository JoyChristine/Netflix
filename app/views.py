from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    return render(request, 'all/index.html')

@login_required(login_url='accounts/login')
def dashboard(request):
    return render(request, 'all/dashboard.html')