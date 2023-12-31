from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<em> Second appasdfasdf for testing djang </em>")
# Create your views here.
