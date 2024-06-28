from django.shortcuts import render, redirect
from requests_oauthlib import OAuth2Session
from django.conf import settings
from .models import Integration
from django.http import JsonResponse, HttpResponse
import json
import logging
from django.views.decorators.csrf import csrf_exempt


# Configure logging
logger = logging.getLogger(__name__)


@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        # Verification step
        print()
        logger.info("WEBHOOK GET REQUEST CALLED")
        print("WE ARE IN WEBHOOK GET REQUEST")
        print()
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if mode and token:
            if mode == 'subscribe' and token == 'VAIBHAV_VERIFICATION_TOKEN':
                return HttpResponse(challenge)
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse("Invalid request", status=400)

    if request.method == 'POST':
        # Handle the incoming webhook data
        data = json.loads(request.body.decode('utf-8'))
        # Process your data here
        logger.info(f"Received webhook data: {data}")

        print(data)
        return JsonResponse({'status': 'success', 'data': data}, status=200)

    return HttpResponse(status=404)


def index(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def get_facebook_auth_url(request):
    redirect_uri = "https://leadsbridge.pythonanywhere.com/"
    facebook = OAuth2Session(settings.FACEBOOK_APP_ID, redirect_uri=redirect_uri)
    authorization_url, state = facebook.authorization_url('https://www.facebook.com/v18.0/dialog/oauth')

    # Save the generated state into the session for later validation in the callback
    request.session['oauth_state'] = state

    # Redirect the user to the authorization URL
    return redirect(authorization_url)


def facebook_callback(request):
    facebook = OAuth2Session(settings.FACEBOOK_CLIENT_ID, state=request.session['oauth_state'])
    token = facebook.fetch_token('https://graph.facebook.com/oauth/access_token',
                                 client_secret=settings.FACEBOOK_APP_SECRET,
                                 authorization_response=request.get_full_path())
    user_info = facebook.get('https://graph.facebook.com/me?fields=id,name,email').json()

    print(token, user_info)
    # Save token and user_info as needed
    return redirect('integration_success.html')


def manage_integrations(request):
    if request.method == "POST":
        # Handle new integration creation here
        pass
    integrations = Integration.objects.filter(user=request.user)
    return render(request, 'manage_integrations.html', {'integrations': integrations})
