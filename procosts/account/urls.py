from django.urls import path
from .views import RegisterUserView,LoginUserView, ChangePhotoView,LogoutUserView
urlpatterns = [
    path('register/',RegisterUserView.as_view()),
    path('login/',LoginUserView.as_view()),
     path('logout/',LogoutUserView.as_view()),
    path('photo/<id>',ChangePhotoView.as_view()),
]
