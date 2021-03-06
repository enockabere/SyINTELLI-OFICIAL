from email import message
import threading
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from . models import Category, Offers,caseStudy, Culture,Mission
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from  django.conf import settings
from django.contrib import messages
from datetime import date
from django.template.loader import render_to_string

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
        
        
# Create your views here.
def landing(request):
    all = Category.objects.all()
    study = caseStudy.objects.all()
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
            print(name,email,phone,message)
        except ValueError:
            messages.error(request, "Not sent. Invalid Input, Try Again!!")
            return redirect('landing')
    if name and email and phone and message:
        try:
            email_subject = 'General Enquiry'
            email_body = render_to_string('mails/enquiry.html', {
            "user": name,
            "message": message,
            'phone': phone,
            "email":email
            })
            email = EmailMessage(subject=email_subject, body=email_body,
                             from_email=settings.DEFAULT_FROM_EMAIL, to=['info@sy-intelli.com'])

            EmailThread(email).start()
            return redirect('landing')
        except BadHeaderError:
            return redirect('landing')
    ctx = {"all":all,"year":year, "study":study}
    return render(request,"index.html",ctx)

def solution(request,pk):
    todays_date = date.today()
    year= todays_date.year
    topic = Category.objects.get(id=pk)
    offer = Offers.objects.filter(Category=pk)
    all = Category.objects.all()
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
            email_subject = f'Quotation for {service}'
            email_body = render_to_string('mails/quote.html', {
            "user": name,
            "message": subject,
            'service': service,
            "email":email
            })
            email = EmailMessage(subject=email_subject, body=email_body,
                             from_email=settings.DEFAULT_FROM_EMAIL, to=['sales@sy-intelli.com'])
            EmailThread(email).start()
            return redirect('solution', pk=pk) 
        except BadHeaderError:
            return redirect('solution', pk=pk)    
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
            print(name,email,phone,message)
        except ValueError:
            messages.error(request, "Not sent. Invalid Input, Try Again!!")
            return redirect('solution', pk=pk)
        try:
            email_subject = 'General Enquiry'
            email_body = render_to_string('mails/enquiry.html', {
            "user": name,
            "message": message,
            'phone': phone,
            "email":email
            })
            email = EmailMessage(subject=email_subject, body=email_body,
                             from_email=settings.DEFAULT_FROM_EMAIL, to=['maebaenock95@gmail.com'])

            EmailThread(email).start()
            return redirect('solution',pk=pk)  
        except BadHeaderError:
            return redirect('solution',pk=pk)    
    return redirect('solution', pk=pk)    
def about_us (request):
    todays_date = date.today()
    year= todays_date.year
    all = Category.objects.all()
    culture = Culture.objects.last()
    mission = Mission.objects.last()
    ctx = {"year":year,"all":all,'culture':culture,"mission":mission}
    return render(request,'about.html',ctx)

def CaseStudy (request,pk):
    todays_date = date.today()
    year= todays_date.year
    case = caseStudy.objects.get(id=pk)
    all = Category.objects.all()
    ctx = {"res":case,"year":year,"all":all}
    return render(request,'case.html',ctx)

def Contact (request):
    todays_date = date.today()
    year= todays_date.year
    all = Category.objects.all()
    offer = Offers.objects.all()
    ctx = {"year":year,"all":all,"offer":offer}
    return render(request,'contact.html',ctx)

def Services (request):
    todays_date = date.today()
    year= todays_date.year
    all = Category.objects.all()
    offer = Offers.objects.all()
    ctx = {"year":year,"all":all,"offer":offer}
    return render(request,'services.html',ctx)

def SingleService (request,pk):
    todays_date = date.today()
    year= todays_date.year
    service = Offers.objects.get(id=pk)
    all = Category.objects.all()
    ctx = {"res":service,"year":year,"all":all}
    return render(request,'single.html',ctx)