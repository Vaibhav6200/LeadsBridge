from django.urls import path
from .views import index


app_name = 'integrations'


urlpatterns = [
    path('', index, name='index'),
]