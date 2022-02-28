from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from . models import ALL_Category, Offers
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from  django.conf import settings
from django.contrib import messages
from datetime import date


# Create your views here.
def landing(request):
    all = ALL_Category.objects.all()
    todays_date = date.today()
    year= todays_date.year
    name= ''
    email = ""
    phone = ""
    message = ""
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
        except ValueError:
            messages.error(request, "Not sent. Invalid Input, Try Again!!")
            return redirect('landing')
    if name and email and phone and message:
        try:
            send_mail(
                f"General Enquiry",
                f"SY-INTELLI CONSULTING, \n\n{message}. \n\nKind Regards,\n{name} \n{phone}.",
                settings.DEFAULT_FROM_EMAIL,
                ['info@sy-intelli.com'],
                fail_silently=False
            )
            messages.success(request, "Thank you for contacting us, we will respond to your request as soon as possible.")
            return redirect('landing')
        except BadHeaderError:
            return redirect('landing')
    ctx = {"all":all,"year":year}
    return render(request,"index.html",ctx)
def solution(request,pk):
    todays_date = date.today()
    year= todays_date.year
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
            messages.success(request, "Thank you for contacting us, we will respond to your request as soon as possible.")
            return redirect('solution', pk=id) 
        except BadHeaderError:
            return redirect('solution', pk=id)    
    ctx = {"res":offer,"topic":topic,
           "all":all,"emails":emails,
           "year":year}
    return render(request,"solution.html",ctx)

def contact(request,pk):
    name= ''
    email = ""
    phone = ""
    message = ""
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
        except ValueError:
            messages.error(request, "Not sent. Invalid Input, Try Again!!")
            return redirect('solution', pk=pk)
    if name and email and phone and message:
        try:
            send_mail(
                f"General Enquiry",
                f"SY-INTELLI CONSULTING, \n\n{message}. \n\nKind Regards,\n{name} \n{phone}.",
                settings.DEFAULT_FROM_EMAIL,
                ['info@sy-intelli.com'],
                fail_silently=False
            )
            messages.success(request, "Thank you for contacting us, we will respond to your request as soon as possible.")
            return redirect('solution',pk=pk)  
        except BadHeaderError:
            return redirect('solution',pk=pk)    
    return redirect('solution', pk=pk)    
   