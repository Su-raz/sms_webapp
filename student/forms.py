from django.contrib.admin.widgets import AdminDateWidget
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


# from datetime import datetime

class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        # empty_permitted = False
        fields = [ 'name' , 'address' , 'phone_number', 'gender', 'date_of_birth' , 'fathername' , 'mothername' , 'shift' , 'course' , 'qualification'  , 'refered_by'] 
        widgets = {'date_of_birth': AdminDateWidget(attrs={'type': 'date'})}



class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'name' , 'address' , 'phone_number', 'gender' ,'date_of_birth', 'fathername' , 'mothername' , 'shift' , 'course' , 'qualification' , 'refered_by' ] 

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']



class DocumentCreationForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['student' , 'name']





class DocumentUpdateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['student' , 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].disabled = True



class PaymentCreateForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['student' , 'course' , 'course_amount' , 'remaining_amount']

class PaymentTransactionForm(forms.ModelForm):
    class Meta:
        model =Payment
        fields =['student' , 'course']
