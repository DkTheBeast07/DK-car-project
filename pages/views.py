from django.shortcuts import render
from .models import Team

# Home view for the pages app
def home(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
        
    }
    return render(request, 'pages/home.html',context=data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')