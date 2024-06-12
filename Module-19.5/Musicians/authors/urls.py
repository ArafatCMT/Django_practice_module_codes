from django.urls import path
from authors import views

urlpatterns = [
    path('registration/', views.RegistrationForm, name='registration'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]