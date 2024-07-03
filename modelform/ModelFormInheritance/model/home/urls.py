from django.contrib import admin
from home import views
from django.urls import path,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('add/',views.student_registration,name="add")

]
