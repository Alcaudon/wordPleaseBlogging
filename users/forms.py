# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    login_username = forms.CharField(label="User name")
    login_password = forms.CharField(widget=forms.PasswordInput(), label="Password")