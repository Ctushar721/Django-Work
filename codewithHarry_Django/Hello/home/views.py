from django.shortcuts import render
from urllib3 import HTTPResponse
from django.shortcuts import HttpResponse, render # New line added

def index(request):
    return HttpResponse('This is homepage')
def about(request):
    return HttpResponse('This is about')



