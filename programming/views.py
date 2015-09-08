# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from programming.models import Programmingforum


def programmingforum(request):
    programmingforu = Programmingforum.objects.all()
    return render_to_response('programming/forum.html', {'programmingforu': programmingforu})


