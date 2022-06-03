from urllib.request import Request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'all/index.html')

# @login_required(login_url='accounts/login')
# def dashboard(request):
#     return render(request, 'all/dashboard.html')

# def movies(request):
#     response=Request.get('https://api.themoviedb.org/3/movie/550?api_key=3dcc48c218d75480e4438171ddc177cf')
#     movies = response.json()
#     print(movies)

#     return render('request', 'all/dashboard.html', {'movies': movies})

