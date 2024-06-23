from django.shortcuts import render,redirect
from django.views.generic import FormView
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def send_transaction_email(user, subject, template):
    message = render_to_string(template, {
        'user': user,
    })
    email = EmailMultiAlternatives(subject, '', to=[user.email])
    email.attach_alternative(message, 'text/html')
    email.send()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid function call hobe jodi thik thake
    
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('login')
    
class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance= request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/passwordChange.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        update_session_auth_hash(self.request, form.user)
        send_transaction_email(self.request.user, 'Password Change Message', 'accounts/change_pass_email.html')
        return super().form_valid(form)


    