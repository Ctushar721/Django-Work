# from django.shortcuts import render_to_response
from urllib3 import HTTPResponse
from django.shortcuts import HttpResponse, render
from home.models import Contact

def index(request):
    context = {
        'x':'Variable'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact( name= name,email=email)
        contact.save()
        print(name,email)
    return render(request, 'index.html', context)
    # return HttpResponse('This is homepage')
def about(request):
    return HttpResponse('This is about')
def contact(request):
    return HttpResponse('This is contact')
def services(request):
    return HttpResponse('This is services')



