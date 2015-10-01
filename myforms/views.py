# -*- coding: utf-8 -*-
# Create your views here.

from myforms.forms import MyNameForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render


# получаем форму после нажатия
def myname(request):
    if request.method == 'POST':
        form = MyNameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/forms/')

    else:
        form = MyNameForm()
    return render(request, 'forms/forms.html', {'form': form})
