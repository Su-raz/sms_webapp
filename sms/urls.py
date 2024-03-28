"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , Index ,  name ="index"),
    # path('convert-date' , convert_date , name ="convert-date"),
    path('add-student/' , AddStudent , name ="add-student"),
    path('list-student/' , ListStudent , name ="list-student"),
    path('edit-student/<str:pk>' , EditStudent , name ="edit-student"),
    path('delete-student/<str:pk>' , DeleteStudent , name ="delete-student"),

    path('student-report' , StudentReport , name ="Report Student"),

    path('add-course/' , AddCourse , name ="add-course"),
    path('add-shift/' , AddShift , name ="add-shift"),
    path('add-document' , AddDocument , name ="add-document" ),
    path('edit-document/<str:pk>' , EditDocument , name = "edit-document"),
    path('delete-document/<str:pk>' , DeleteDocument , name = "delete-document"),
    path('list-document' , ViewDocument , name ="list-document" ),
    path('payment' , AddPayment , name ="payment"),
    path('list-payment' , ViewPayment , name ="list-payment"),
    path('payment-tr' , PaymentTransaction , name ="payment-tr"),
    path('payment-report' , PaymentReport , name = "payment-report"),





]
