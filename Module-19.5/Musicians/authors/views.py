from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from authors import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages 
from django.urls import reverse_lazy

# Create your views here.
def RegistrationForm(request):
    if request.method == 'POST':
        form = forms.Registration(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            messages.success(request,'Account Created Successfully Please Login')
            return redirect('login')
    else:
        form = forms.Registration()
    return render(request, 'registration.html', {'form': form})

class UserLogin(LoginView):
    template_name = 'login.html'

    def get_redirect_url(self):
        return reverse_lazy('profile')
        
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in information is incurrect')
        return super().form_invalid(form)
    
class UserLogout(LogoutView):
    def get_redirect_url(self):
        messages.success(self.request, "Logged Out Successful")
        return reverse_lazy('login')
    
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


