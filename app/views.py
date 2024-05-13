from django.shortcuts import redirect, render

from app.models import product
def ecommerce(request):
    data=product.objects.all()
    context={"data":data}
    return render(request,"ecommerce.html",context)
def about(request):
    return render(request,"about.html")
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        price=request.POST.get('price')
        query=product(name=name,id=id,price=price)
        query.save()
    return render(request,"ecommerce.html")
def updateData(request,id):
     d=product.objects.get(id=id)
     context={"d":d}
     if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        price=request.POST.get('price')

        edit=product.objects.get(id=id)
        edit.name=name
        edit.id=id
        edit.price=price
        edit.save()
      
     return render(request,"edit.html",context)
def deleteData(request,id):
    d=product.objects.get(id=id)
    d.delete()
    return redirect("/")
