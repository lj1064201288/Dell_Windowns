from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def do_phone(request):
    return HttpResponse('电话:13550211725')

def do_year(request):
    return HttpResponse('1996年2月24日')
