from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Kitob_form
from .models import *


def home(request, ism):
    return render(request, "home.html", {'name': ism})
def kitoblar(request):
    if request.method == 'POST':
        form = Kitob_form(request.POST)
        if form.is_valid():
            forma.save()
        return redirect('kitoblar')
    kitob = Kitob.objects.all()
    forma = Kitob_form()
    return render(request, "kitoblar.html", {'kitob': kitob, "forma": forma})
def mualliflar(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism=request.POST.get('m_ism'),
            yosh=request.POST['m_yosh'],
            jins=request.POST['m_jins']
        )
        return redirect('mualliflar')
    muallif = Muallif.objects.all()
    return render(request, "mualliflar.html", {'muallif': muallif})
def kitob1(request, son):
    k1 = Kitob.objects.get(id=son)
    k1.delete()
    return redirect('kitoblar')

def muallif1(request, son):
    m1 = Muallif.objects.get(id=son)
    m1.delete()
    return redirect('mualliflar')

def record1(request, son):
    r1 = Record.objects.get(id=son)
    r1.delete()
    return redirect('recordlar')


def recordlar(request):
    record = Record.objects.all()
    return redirect(request, "recordlar.html", {'record': record})

def kitob(request):
    return HttpResponse(Kitob.objects.first())
def muallif(request):
    return HttpResponse(Muallif.objects.first())
def katta_muallif(request):
    return HttpResponse(Muallif.objects.order_by('yosh').last())
def record(request):
    return HttpResponse(Record.objects.first())
def ilmiy(request):
    return HttpResponse(Kitob.objects.filter(tur='Non-fiction').first())
def erkak(request):
    return HttpResponse(Muallif.objects.filter(jins='Erkak').first())