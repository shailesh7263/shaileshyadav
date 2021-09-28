from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView

from django.core.mail import EmailMessage

def index(request):
    return render(request,'index.html')

def send_gmail(request):
    if request.method=="POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        resumeFile = request.FILES['resumeFile']
        
        

        message = f"Resume received from : {name}\n\nThe resume is attached with this email. Please check it out."

        mail:"EmailMessage" = EmailMessage(
            subject, 
            message, 
            "yadavshailesh7263@gmail.com", 
            ['rsinghm4u@gmail.com']
            )
        mail.attach(resumeFile.name, resumeFile.read(), resumeFile.content_type)
        mail.send()
     
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse('Invalid request')
