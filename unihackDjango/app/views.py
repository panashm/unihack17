# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from app.models import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def index(request):
    current_user = request.user
    return render(request, 'index.html', {'current_user' : current_user})

@login_required
def dashboard(request):
        #BadgeClaim.objects.filter(consumer=)
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()
    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        badges = consumer.badge.all()
        return render(request, 'dashboard.html', {'consumer' : consumer, 'badges' : badges, 'current_user' : current_user})
    else:
        return render(request, 'index.html', {'consumer' : None, 'current_user' : current_user})

def discover(request):
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()
    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        return render(request, 'discover.html', {'consumer' : consumer, 'current_user' : current_user})
    else:
        return render(request, 'discover.html', {'consumer' : None, 'current_user' : current_user})

def discoverQuery(request, search_string):
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()
    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        return render(request, 'discover.html', {'consumer' : consumer, 'current_user' : current_user})
    else:
        return render(request, 'discover.html', {'consumer' : None, 'current_user' : current_user})

def badge(request, badge_id):
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()
    bad = get_object_or_404(Badge, pk=badge_id)
    issues = BadgeClaim.objects.filter(badge=bad).count()
    supporting_businesses = Business.objects.filter(badge=bad)

    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        return render(request, 'badge.html',
            {"badge" : bad,
            "issues" : issues,
        "businesses" : supporting_businesses,
          'consumer' : consumer,
      'current_user' : current_user}
        )
    else:
        return render(request, 'badge.html',
            {"badge" : bad,
            "issues" : issues,
        "businesses" : supporting_businesses,
          'consumer' : None,
      'current_user' : current_user}
        )

def organisation(request, organisation_id):
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()

    org = get_object_or_404(Organisation, pk=organisation_id)

    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        return render(request, 'organisation.html', {'organisation' : org, 'consumer' : consumer, 'current_user' : current_user})
    else:
        return render(request, 'organisation.html', {'organisation' : org, 'consumer' : None, 'current_user' : current_user})


def business(request, business_id):
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()

    bus = Business.objects.get(pk=business_id)

    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        return render(request, 'business.html', {'business' : bus, 'consumer' : consumer, 'current_user' : current_user})
    else:
        return render(request, 'business.html', {'business' : bus, 'consumer' : None, 'current_user' : current_user})

@login_required
def businesses(request):
    return render(request, 'businesses.html', {})

def about(request):
    current_user = request.user
    isConsumer = Consumer.objects.filter(user=current_user).count()
    if isConsumer > 0:
        consumer = Consumer.objects.get(user=current_user)
        return render(request, 'about.html', {'consumer' : consumer, 'current_user' : current_user})
    else:
        return render(request, 'about.html', {'consumer' : None, 'current_user' : current_user})


def login_view(request, onsuccess='/', onfail='/login/'):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print("USER LOGGED IN")
        return redirect('dashboard/')
    else:
        print("USER FAILED TO LOGGED IN")
        return render(request, 'login.html', {})

@login_required
def logout_view(request):
    print("A user logged out.")
    logout(request)
    return redirect('login')

def register(request):
    return render(request, 'index.html', {})
