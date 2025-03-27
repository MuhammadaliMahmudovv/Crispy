from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

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