from django.shortcuts import render
from requests_oauthlib import OAuth2Session
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def get_facebook_auth_url(request):
    redirect_uri = "https://yourcallbackurl.com"
    facebook = OAuth2Session(settings.FACEBOOK_CLIENT_ID, redirect_uri=redirect_uri)
    authorization_url, state = facebook.authorization_url('https://www.facebook.com/dialog/oauth')
    return authorization_url
