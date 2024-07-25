from django.urls import path
from . import views

urlpatterns = [
    path('getAll/<ui>',views.getAll),
    path('add/<pk>/<ui>',views.create),
    path('update/<id>/<ui>',views.update),
    path('delete/<id>/<ui>',views.delete),    
]