from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm
from collections import OrderedDict


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['class'] = 'email-field email-large'
        self.fields['password'].widget.attrs['class'] = 'email-field email-large'
        self.fields['login'].label = "Email"
        self.fields['remember'].label = ''
        self.fields['login'].widget.attrs['placeholder'] = 'Email Address'


class UserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserSignupForm, self).__init__(*args, **kwargs)

        del self.fields['password2']

        self.fields['first_name'] = forms.CharField(label='First Name', required=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'size': '45',
                   'placeholder': 'First Name'}))
        self.fields['last_name'] = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'size': '45',
                   'placeholder': 'Last Name'}))

        self.fields['first_name'].widget.attrs['class'] = 'email-field email-large'
        self.fields['last_name'].widget.attrs['class'] = 'email-field email-large'
        self.fields['email'].label = "Email"
        self.fields['email'].widget.attrs['class'] = 'email-field email-large'
        self.fields['password1'].widget.attrs['class'] = 'email-field email-large'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'

        original_fields = self.fields
        new_order = OrderedDict()
        for key in ['first_name', 'last_name', 'email', 'password1']:
            new_order[key] = original_fields[key]
        self.fields = new_order

class UserPasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'email-field email-large'

class UserPasswordResetFromKey(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserPasswordResetFromKey, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'email-field email-large'
        self.fields['password2'].widget.attrs['class'] = 'email-field email-large'