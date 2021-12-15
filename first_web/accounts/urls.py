from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns=[    
    path('login/',views.loginApp,name='web-login'),
    path('logout/',views.logoutApp,name="web-logout"),
    path('signup/',views.signup,name='web-signup'),
    path('user-created/',views.usercreated,name='user-created'),
]

