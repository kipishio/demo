# -*- coding: utf-8 -*-
__author__ = 'Юля'
from django import forms


class MyNameForm(forms.Form):
    name = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.Textarea)

