from django.contrib import admin
from django.urls import path, include
from lms import views  # Import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lms/', include('lms.urls', namespace='lms')),  # ✅ Correct
    path('', views.home, name='home'),  # ✅ Homepage route
]
