from django.urls import path
from . import views

app_name = "lms"  # ✅ This must be included

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.user_registration, name='user_registration'),
]
