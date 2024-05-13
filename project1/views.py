

from django.shortcuts import render

from app.models import product

def app(request):
    data=product.objects.all()
    context={"data":data}
    return render(request,"ecommerce.html",context)

def about(request):
    return render(request,"about.html")