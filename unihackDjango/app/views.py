# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def dashboard(request):
    return render(request, 'index.html', {})


def discover(request):
    return render(request, 'index.html', {})

def discoverQuery(request, search_string):
    return render(request, 'index.html', {})


def badge(request, badge_id):
    return render(request, 'index.html', {})


def organisation(request, organisation_id):
    return render(request, 'index.html', {})

def business(request, business_id):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'index.html', {})

def logout(request):
    return render(request, 'index.html', {})

def register(request):
    return render(request, 'index.html', {})

    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),

    url(r'^discover/$', views.discover, name='discover'),
    url(r'^discover/s/(\s+)/$', views.discoverQuery, name='discoverQuery'),
