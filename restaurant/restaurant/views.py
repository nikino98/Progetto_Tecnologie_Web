from django.shortcuts import render


def prova(request):
    return render(request, 'home.html')