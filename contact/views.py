from django.http import HttpResponse
from django.shortcuts import render

def send_msg(request):
    return HttpResponse("<html><head><title") 