from django.contrib import admin
from django.urls import path, include
from authentication_project.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('', home, name='homepage'),
]
