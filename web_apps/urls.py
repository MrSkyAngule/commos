from django.urls import path, include

from web_apps.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]