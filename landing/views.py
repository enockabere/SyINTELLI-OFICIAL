from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from . models import ALL_Category, Offers
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from  django.conf import settings
from django.contrib import messages

# Create your views here.
def landing(request):
    all = ALL_Category.objects.all()
    ctx = {"all":all}
    return render(request,"index.html",ctx)
def solution(request,pk):
    topic = ALL_Category.objects.get(id=pk)
    offer = Offers.objects.filter(group=pk)
    all = ALL_Category.objects.all()
    emails = Offers.objects.all() 
    name= ''
    email = ""
    service = ""
    subject = ""
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            service = request.POST.get('service')
            subject = request.POST.get('subject')
        except ValueError:
            messages.error(request, "Not sent. Invalid Input, Try Again!!")
            return redirect('solution', pk=id)
    if name and email and service and subject:
        try:
            send_mail(
                f"Quotation for {service}",
                f"SY-INTELLI CONSULTING, \n\nTrust you are well, \n\nI'm requesting for a quotation on {service} to be sent to {email}. \n\nWith the following comments: {subject}.\n\nBest regards \n{name}.",
                settings.DEFAULT_FROM_EMAIL,
                ['sales@sy-intelli.com'],
                fail_silently=False
            )
            print("True")
        except BadHeaderError:
            return redirect('solution', pk=id)    
    ctx = {"res":offer,"topic":topic,"all":all,"emails":emails}
    return render(request,"solution.html",ctx)
