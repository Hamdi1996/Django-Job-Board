from django.shortcuts import render
from django.conf import settings
from .models import Info
from django.core.mail import send_mail

def send_msg(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        try:
            send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
        except Exception as e:
            print (str(e))
            
    return render(request, 'contact/contact.html', {"myinfo": myinfo})
