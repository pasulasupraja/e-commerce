from django.urls import path
from app import views

urlpatterns = [
    path('',views.ecommerce),
    path('about/',views.about,name='about'),
    path('insert/',views.insertdata,name='insert'),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deleteData'),

]
