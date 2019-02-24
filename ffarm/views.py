from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import json, requests
from ffarm.models import User

def index(request):

    client_id='04e5bff184fc4ac08e9c95ac49644d16'
    redirect_uri='http://localhost:8000/login/instagram-success'
    final_uri='https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code'.format(client_id, redirect_uri)

    return render(request, 'index.html', {'URI':final_uri})

def instagram_success(request):
    code = request.GET.get('code')
    request_body = {'client_id':'04e5bff184fc4ac08e9c95ac49644d16',
            'client_secret':'178c6c3ae2f44df8a1dc5c1061f52168',
            'grant_type':'authorization_code',
            'redirect_uri':'http://localhost:8000/login/instagram-success',
            'code':code
            }

    response = requests.post('https://api.instagram.com/oauth/access_token', request_body)
    response_dict = json.loads(response.text)
    
    user = User(username=response_dict.user.username, token=response_dict.access_token, profile_picture=response_dict.user.profile_picture)
    user.save()

    return render(request, 'success.html', {'user':user})
