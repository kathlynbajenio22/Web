from django.contrib import admin
from django.urls import path, include
from lms.views import home, user_registration, user_login  # ✅ Rename `login` to `user_login`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lms/', include('lms.urls', namespace='lms')),  # ✅ Include app URLs
    path('', home, name='home'),  # ✅ Homepage route
    path('user_registration/', user_registration, name='user_registration'),  # ✅ Signup route
    path('user_login/', user_login, name='user_login'),  # ✅ Login route (avoid Django's `login` conflict)
]
