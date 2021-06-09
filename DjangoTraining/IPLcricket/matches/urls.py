#!/usr/bin/python
"""
Purpose:
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('winning_team/', views.winning_team, name='winning_team'),
]