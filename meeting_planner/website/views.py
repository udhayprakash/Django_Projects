from django.http import HttpResponse 
from datetime import datetime 
from django.shortcuts import render 

def welcome(request):
    # return HttpResponse('Welcome to the Meeting Planner!')
    return render(request, "website/welcome.html")

def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))

def about(request):
    return HttpResponse('I am Udhay from Hyderabad, India')