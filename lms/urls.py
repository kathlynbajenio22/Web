from django.urls import path
from .views import home, user_registration, login, logout

app_name = "lms"  # ✅ This must be included

urlpatterns = [
    path('', home, name='home'),
    path('user_registration', user_registration, name='user_registration'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
   
]
