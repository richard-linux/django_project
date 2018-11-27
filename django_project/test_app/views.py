from django.shortcuts import render
from easygui import *

def home(request):
    return render(request, 'test_app/home.html')

    

    
    
