from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

   path('',views.register_view,name='register_view'),
   path('delete/<int:reg_id>/', views.delete, name='delete'),
   path('update/<int:id>/', views.update, name='update')
]