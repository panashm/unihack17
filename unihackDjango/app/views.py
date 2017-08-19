# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def user(request):
    return render(request, 'user.html', {})

def login(request):
    return render(request, 'index.html', {})

def business(request):
    return render(request, 'index.html', {})

def organisation(request):
    return render(request, 'index.html', {})
# Create your views here.
