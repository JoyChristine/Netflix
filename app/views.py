from urllib.request import Request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import requests
# Create your views here.
def welcome(request):
    return render(request, 'all/index.html')

@login_required(login_url='accounts/login')
def movies(request):
    response=requests.get('https://api.themoviedb.org/3/trending/all/week?api_key=3dcc48c218d75480e4438171ddc177cf')
    movies = response.json()['results']
    filtered = []
    for i in range(12):
        filtered.append(movies[i])
    print(movies)

    return render(request, 'all/index.html', {'movies': filtered})

# def upcoming(request):
#     # 

#     response=requests.get('https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}?api_key=3dcc48c218d75480e4438171ddc177cf')
#     movies = response.json()['results']
#     filtered = []
#     for i in range(12):
#         filtered.append(movies[i])
#     print(movies)

#     return render(request, 'all/dashboard.html', {'upcoming': filtered})

  