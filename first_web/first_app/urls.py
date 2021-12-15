from django.urls import path
from django.conf.urls import url
from first_app import views


urlpatterns = [
    path('',views.home,name='web-home'),
    path('comic/',views.comic,name='web-comic'),
    path('drawing/',views.drawing,name='web-drawing'),
    path('photo/',views.photo,name='web-photo'),
    path('user-profile/',views.userProfile,name='user-profile'),
    
]