# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from app.models import *

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html', {})

@login_required
def dashboard(request):
    #isConsumer = Consumer.objects.filter(user=user).count()
    #if isConsumer > 0:
        
    
    #BadgeClaim.objects.filter(consumer=)
    return render(request, 'dashboard.html', {})

def discover(request):
    return render(request, 'discover.html', {})

def discoverQuery(request, search_string):
    return render(request, 'index.html', {})

def badge(request, badge_id):
    bad = get_object_or_404(Badge, pk=badge_id)
    issues = BadgeClaim.objects.filter(badge=bad).count()
    supporting_businesses = Business.objects.filter(badge=bad)
    return render(request, 'badge.html',
        {"badge" : bad,
        "issues" : issues,
    "businesses" : supporting_businesses}
    )

def organisation(request, organisation_id):
    org = get_object_or_404(Organisation, pk=organisation_id)
    return render(request, 'organisation.html', {'organisation' : org})

def business(request, business_id):
    bus = Business.objects.get(pk=business_id)
    return render(request, 'business.html', {'business' : bus})

@login_required
def businesses(request):
    return render(request, 'businesses.html', {})

def about(request):
    return render(request, 'about.html', {})


def login(request, next_page='login'):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'dashboard.html', {})
    else:
        return render(request, 'login.html', {})

@login_required
def logout(request):
    return redirect('login')

def register(request):
    return render(request, 'index.html', {})
