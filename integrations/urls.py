from django.urls import path
from .views import index, get_facebook_auth_url, facebook_callback, manage_integrations, webhook, login_view


app_name = 'integrations'


urlpatterns = [
    path('', index, name='index'),
    path('get-facebook-auth-url/', get_facebook_auth_url, name='get_facebook_auth_url'),
    path('facebook-callback/', facebook_callback, name='facebook_callback'),
    path('manage-integrations/', manage_integrations, name='manage_integrations'),
    path('webhook/', webhook, name='webhook'),
    path('login/', login_view, name='login'),
]
