# from django.shortcuts import render_to_response
from urllib3 import HTTPResponse
from django.shortcuts import HttpResponse, render

def index(request):
    context = {
        'x':'Variable'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is homepage')
def about(request):
    return HttpResponse('This is about')
def contact(request):
    return HttpResponse('This is contact')
def services(request):
    return HttpResponse('This is services')



