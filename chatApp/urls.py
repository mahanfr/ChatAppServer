from django.contrib import admin
from django.urls import path , include
from chat import views as ChatViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/chat/',include('chat.urls')),
    path('api/v1/users/',include('user.urls')),
]
