from django.urls import path
from . import views

urlpatterns = [
    path('getAll/<id>',views.getAll),
    path('add/<pk>/<ui>',views.create),
    path('update/<id>',views.update),
    path('delete/<id>',views.delete),    
]