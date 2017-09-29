# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.account.views import SignupView, LoginView, logout, PasswordResetView, PasswordResetDoneView, \
    PasswordResetFromKeyView, PasswordResetFromKeyDoneView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rodapp.forms import *

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class UserSignup(SignupView):
    template_name = 'signup.html'
    form_class = UserSignupForm

class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm

class UserPasswordReset(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = UserPasswordResetForm

class UserPasswordResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class UserPasswordResetKey(PasswordResetFromKeyView):
    template_name = 'password_reset_from_key.html'
    form_class = UserPasswordResetFromKey

class UserPasswordResetKeyDone(PasswordResetFromKeyDoneView):
    template_name = 'password_reset_from_key_done.html'

def dashboard(request):
    return render(request, 'dashboard.html')

def is_user_authenticated(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect('/accounts/login/')


