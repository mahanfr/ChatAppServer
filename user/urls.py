from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]