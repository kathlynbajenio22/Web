from django.contrib import admin
from django.urls import path, include
from lms.views import home, user_registration  # ✅ Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lms/', include('lms.urls', namespace='lms')),  # ✅ Correct
    path('', home, name='home'),  # ✅ Homepage route
    path('user_registration/', user_registration, name='user_registration'),  # ✅ Now user_registration is defined
]
