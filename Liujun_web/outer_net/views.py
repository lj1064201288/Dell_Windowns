from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse

# Create your views here.

#html = open('./taobao.html', 'r', encoding='utf-8')
#text= html.read()
#print(text)
#html.close()

def do_taobao(request):
    return HttpResponse("sda")