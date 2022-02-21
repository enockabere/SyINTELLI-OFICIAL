from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from . models import ALL_Category, Offers

# Create your views here.
def landing(request):
    all = ALL_Category.objects.all()
    ctx = {"all":all}
    return render(request,"index.html",ctx)
def solution(request,pk):
    topic = ALL_Category.objects.get(id=pk)
    offer = Offers.objects.filter(group=pk)
    all = ALL_Category.objects.all()
    ctx = {"res":offer,"topic":topic,"all":all}
    return render(request,"solution.html",ctx)