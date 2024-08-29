from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # Your other URL patterns...
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
