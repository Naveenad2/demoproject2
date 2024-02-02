from django.urls import path,include
from . import views

urlpatterns = [
  
    path('',views.main_page,name='main_page'),
    path('register',views.Register,name='register_page'),
    path('login',views.Login,name='login page'),
    path('lectures_cat',views.lectures_cat,name='lectures_cat'),
     path('Logout_',views.Logout_,name='Logout_'),
        path('get_video/<int:id>',views.get_video,name='get_video'),
     path('play_video/<int:id>',views.play_video,name='play_video'),
    
    
    
]