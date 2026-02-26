from django.shortcuts import render

def home(request):
    return render(request, 'store_app/index.html')

def shop(request):
    products = [
        {"name": "Luxury Hoodie", "price": 120},
        {"name": "Urban Jacket", "price": 200},
        {"name": "Casual T-Shirt", "price": 60},
    ]
    return render(request, 'store_app/shop.html', {"products": products})

def about(request):
    return render(request, 'store_app/about.html')
