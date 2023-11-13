from django.shortcuts import render
from .models import Info


def send_msg(request):
    myinfo = Info.objects.first()
    return render(request, 'contact/contact.html', {"myinfo": myinfo})