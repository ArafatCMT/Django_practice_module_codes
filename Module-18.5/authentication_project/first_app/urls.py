from django.urls import path
from first_app.views import signup, Login, profile, Logout, ChangePassword_1, ChangePassword_2

urlpatterns = [
   path('signup/', signup , name = 'signup'), 
   path('profile/', profile , name = 'profile'), 
   path('login/', Login , name = 'login'), 
   path('logout/', Logout , name = 'logout'), 
   path('ChangePassword1/', ChangePassword_1 , name = 'ChangePassword_1'), 
   path('ChangePassword2/', ChangePassword_2 , name = 'ChangePassword_2'), 
]