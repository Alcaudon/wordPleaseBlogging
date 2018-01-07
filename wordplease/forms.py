# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from wordplease.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']
