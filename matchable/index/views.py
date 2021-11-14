from django.shortcuts import render
from .models import Institute

def main(request) :
    return render(request, 'index/main.html')

def list(request) :
    institute = Institute.objects.all()
    return render(request, 'index/list.html', {'institutes' : institute})