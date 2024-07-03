from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.sign_up,name="signup"),
    path('login/',views.user_login,name="login"),
    path('profile/',views.userProfile,name="profile")
]
