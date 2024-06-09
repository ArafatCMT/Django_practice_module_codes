from django.shortcuts import render, redirect
from first_app.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                # print(form.cleaned_data)
                form.save()
                messages.success(request, 'Account Created Successfully Please Login')
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')

def Login(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_passwd = form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_passwd)
            
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    else:
        return redirect('profile')

@login_required            
def profile(request):
    return render(request,'./profile.html', {'user': request.user})

def Logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('homepage')

@login_required
def ChangePassword_1(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(user=request.user, data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request,'./passChange.html', {'form': pass_form})

@login_required
def ChangePassword_2(request):
    if request.method == 'POST':
        pass_form = SetPasswordForm(user=request.user, data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('profile')
    else:
        pass_form = SetPasswordForm(user=request.user)
    return render(request,'./passChange.html', {'form': pass_form})
