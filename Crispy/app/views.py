from django.shortcuts import render
from .models import reservation

def index(request):
    table_reservation = reservation.objects.all()
    if request.method == "POST" and table_reservation:
        table_reservation.save()
        return table_reservation()
    
    return render(request, 'app/index.html', {"table_reservation": table_reservation})

def about(request):
    return render(request, 'app/about.html')

def menu(request):
    return render(request, 'app/menu.html')

def news(request):
    return render(request, 'app/news.html')

def contact(request):
    return render(request, 'app/contact.html')

def news_detail(request):
    return render(request, 'app/news_detail.html') 