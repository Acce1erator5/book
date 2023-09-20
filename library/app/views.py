from django.shortcuts import render
from app.models import *
# Create your views here.


def func_1(request):
    context = {'books': Book.objects.all()}
    return render(request, 'about_page.html', context=context)
