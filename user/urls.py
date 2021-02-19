from django.urls import path,include

from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]