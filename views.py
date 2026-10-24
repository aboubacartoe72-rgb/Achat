from django.shortcuts import render

def page_essaye(request):
    return render(request, 'essaye.html')

def page_panier(request):
    return render(request, 'panier.html')