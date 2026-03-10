from django.urls import path, include

from web_apps.views import dashboard, sse_view

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('event/', sse_view, name='sse_view'),
]