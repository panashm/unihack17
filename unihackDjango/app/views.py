# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from app.models import *

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# Add a comment
@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
def dashboard(request):
    return render(request, 'index.html', {})

@login_required
def discover(request):
    return render(request, 'index.html', {})

@login_required
def discoverQuery(request, search_string):
    return render(request, 'index.html', {})

@login_required
def badge(request, badge_id):
    return render(request, 'index.html', {})

@login_required
def organisation(request, organisation_id):
    org = Organisation.objects.get(pk=organisation_id)
    return render(request, 'organisation.html', {'organisation' : org})

@login_required
def business(request, business_id):
    bus = Business.objects.get(pk=business_id)
    return render(request, 'business.html', {'business' : bus})


def login(request, next_page='login'):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'dashboard.html', {})
    else:
        return render(request, 'login.html', {})

def logout(request):
    return redirect('login')

def register(request):
    return render(request, 'index.html', {})
