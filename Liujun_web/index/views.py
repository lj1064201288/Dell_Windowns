from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def do_index(request):

    return HttpResponse("This is my home")