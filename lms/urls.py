from django.urls import path
from .views import home, user_registration, user_login, logout

app_name = "lms"  # ✅ This must be included

urlpatterns = [
    path('', home, name='home'),
    path('user_registration', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),  # ✅ Now matches the expected URL
    path('logout', logout, name='logout'),
   
]
