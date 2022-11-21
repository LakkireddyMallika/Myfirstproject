from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saturday(request):
    return HttpResponse('Today is Saturday')
