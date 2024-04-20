from django.urls import path
from . import views

urlpatterns = [
    path('getAll',views.getAll),
    path('create',views.create),
    path('update/<id>',views.update),
    path('delete/<id>',views.delete),
    path('addORupdate/<pk>',views.addORupdate),
    path('getuserfinance/<pk>',views.getUserFinance),
]