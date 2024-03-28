from django.db import models

# Create your models here.
class  Shift(models.Model):
	name =models.CharField(max_length= 100 , blank=True , null=True)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length= 100 , blank=True , null=True)

	def __str__(self):
		return self.name

class Gender(models.Model):
	name = models.CharField(max_length= 100 , blank=True , null=True)

	def __str__(self):
		return self.name





class Student(models.Model):
	name =models.CharField(max_length= 50 , null = True , blank =True)
	address = models.CharField(max_length= 100 , blank=True , null=True)
	phone_number =models.CharField(max_length = 20 , blank = True , null=True)
	gender = models.ForeignKey(Gender , on_delete = models.CASCADE)
	date_of_birth = models.DateField("Date of Birth (AD)",auto_now_add = False , auto_now = False , null =True , blank = True)
	fathername = models.CharField( max_length= 100 , null = True , blank =True)
	mothername =models.CharField(max_length= 100 , blank=True , null=True)
	shift = models.ForeignKey(Shift , on_delete = models.CASCADE)
	course = models.ForeignKey(Course , on_delete = models.CASCADE)
	qualification = models.CharField(max_length= 100 , blank=True , null=True)
	refered_by = models.CharField(max_length= 100 , blank=True , null=True)
	def __str__(self):
		return self.name

	# payment = models.ForeignKey(
    #     Payment,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    # )

	

class Document(models.Model):
	student = models.ForeignKey(Student, on_delete = models.CASCADE)
	name = models.TextField(max_length= 3000 , blank=True , null=True) 
	received_date = models.DateTimeField(auto_now_add = True , auto_now = False)

	def __str__(self):
		return self.name 


class Payment(models.Model):
	student = models.ForeignKey(Student ,  on_delete = models.CASCADE)
	course = models.ForeignKey(Course , on_delete = models.CASCADE)
	course_amount = models.FloatField(blank = True , null = True , default= "0")
	remaining_amount =models.FloatField(blank = True , null = True , default= "0")
	received_date = models.DateTimeField(auto_now_add = True )
	last_updated = models.DateTimeField( auto_now = True)
	class Meta:
		unique_together = ['student', 'course']

	def __str__(self):
		return str(self.student)



class Payment_History(models.Model):
	bill_no = models.IntegerField(blank = True , null=True)
	student_name = models.CharField(max_length= 100 , blank=True , null=True)
	course_name = models.CharField(max_length= 100 , blank=True , null=True)
	paid_amount = models.FloatField(blank = True , null = True , default ="0")
	paid_date = models.DateTimeField(auto_now_add=True , auto_now=False)

	def __str__(self):
		return self.student_name








		