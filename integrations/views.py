from django.shortcuts import render, redirect
from requests import session
from requests_oauthlib import OAuth2Session
from django.conf import settings
from .models import Integration


def index(request):
    return render(request, 'index.html')


def get_facebook_auth_url(request):
    redirect_uri = "https://yourcallbackurl.com"
    facebook = OAuth2Session(settings.FACEBOOK_CLIENT_ID, redirect_uri=redirect_uri)
    authorization_url, state = facebook.authorization_url('https://www.facebook.com/dialog/oauth')
    return authorization_url


def facebook_callback(request):
    facebook = OAuth2Session(settings.FACEBOOK_CLIENT_ID, state=session['oauth_state'])
    token = facebook.fetch_token('https://graph.facebook.com/oauth/access_token',
                                 client_secret=settings.FACEBOOK_CLIENT_SECRET,
                                 authorization_response=request.get_full_path())
    user_info = facebook.get('https://graph.facebook.com/me?fields=id,name,email').json()
    # Save token and user_info as needed
    return redirect('integration_success.html')


def manage_integrations(request):
    if request.method == "POST":
        # Handle new integration creation here
        pass
    integrations = Integration.objects.filter(user=request.user)
    return render(request, 'manage_integrations.html', {'integrations': integrations})
