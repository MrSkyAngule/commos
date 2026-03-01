from django.urls import path, include
from rest_framework import routers

from apis.views import send_Views

router = routers.DefaultRouter()
router.register(r'messages', send_Views)

urlpatterns = [
    path('api/', include(router.urls)),
]