from django.contrib import admin
from .models import *

# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    list_display = ['name' , 'address' ,'phone_number', 'fathername' , 'mothername' ,'gender' ,'date_of_birth','shift', 'course' ,'qualification']
    model = Student
    # list_filter = ['course' , 'shift' ,'gender']
    search_fields =['name']


class DocumentAdmin(admin.ModelAdmin):
	model = Document
	list_display = ['student', 'name' , 'received_date']
	search_fields =['student']


class PaymentAdmin(admin.ModelAdmin):
	model = Payment ,
	list_display = ['student', 'course' ,'course_amount' ]
	search_fields =['student' , 'course',]



   

admin.site.register(Student, StudentAdmin)
admin.site.register(Gender)
admin.site.register(Course)
admin.site.register(Payment , PaymentAdmin)
admin.site.register(Payment_History)
admin.site.register(Shift)
admin.site.register(Document , DocumentAdmin)
