from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def salom(request):
    return HttpResponse("Assalomu alaykum Schoolga xush kelibsiz!")

def class_info(request):
    return HttpResponse("Schoolda 20 ta sinf bor")


