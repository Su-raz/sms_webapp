from django.shortcuts import render ,redirect
from django.db import IntegrityError
from django.contrib import messages
from .forms  import*
from .models import*





def Index(request):
	total_student = Student.objects.count()
	document_submited = Document.objects.count()

	course_available = Course.objects.count()

	contex = {
	"total_student":total_student,
	"document_submited":document_submited,
	"course_available":course_available,
	}

	return render(request , 'index.html' , contex)




def AddStudent(request):
	msg =""
	forms = StudentCreationForm(request.POST or None)
	if request.method == "POST":
		name = forms['name'].value()


		father_name = forms['fathername'].value()

		# print(type(date_of_birth))
		if forms.is_valid():
			data =Student.objects.filter(name =name)
			if data:
				for instance in data:

					if instance.name == name and instance.fathername == father_name:
						msg ="user is already exist"
						
						
					else:
						forms.save()
						print("saved")
						return redirect('/list-student/')
			else:
					forms.save()
					print("saved")
					return redirect('/list-student/')

	context ={
	'msg' :msg,
	'form':forms,

	}
	return render(request , 'add_student.html' , context)


def ListStudent(request):

	queryset = Student.objects.all()
	context ={
	"queryset":queryset,
	}
	return render(request , 'list_student.html' , context)


def EditStudent(request , pk):
	queryset = Student.objects.get(id =pk)
	form = StudentUpdateForm(instance = queryset)


	if request.method =="POST":
		form =StudentUpdateForm(request.POST , instance = queryset)
		if form.is_valid():
			form.save()
			return redirect('/list-student')
	context ={
	"form":form,
	}
	return render(request , "Edit_student.html" , context)


def DeleteStudent(request , pk ):
	queryset = Student.objects.get(id = pk)
	if request.method == "POST":
		queryset.delete()
		return  redirect('list-student')
	context ={}
	return render(request , 'delete_student.html' , context)
def StudentReport(request):

	queryset = Student.objects.all()
	context ={
	"queryset":queryset,
	}
	return render(request , 'student_report.html' , context)


# student views end
def AddCourse(request):
	context ={}
	if request.method =="POST":
		course_name = request.POST['course']
		try:
			validate = Course.objects.get(name = course_name)
			msg = "course is already registered"
			context ={
			'msg':msg,
			}
		except:

			course = Course(name = course_name)
			course.save()
			return redirect('/add-student/')

			
		


	# form = CourseCreationForm(request.POST or None)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect ('/add-student')

	# context ={
	# 'form':form
	# }

	return render(request , 'add_course.html' , context )



def AddShift(request):
	context ={}
	if request.method =="POST":
		shift_name = request.POST['shift']
		try:
			validate= Shift.objects.get(name = shift_name)
			msg = "Shift is already registered"
			context ={
			'msg':msg,
			}
		except:
			course = Shift(name = shift_name)
			course.save()
			return redirect('/add-student/')


	return render(request , 'add_shift.html' , context)




# documents views start
def AddDocument(request):
	forms = DocumentCreationForm(request.POST or None)
	context ={
	'form':forms
	}
	try:
		document = Document.objects.get(student = forms['student'].value())
		forms = DocumentCreationForm()
		msg = "Sorry you added before,if you want to add more then go through edit option "
		context = {
		'msg': msg , 
		'form':forms,
		}
	except:
		if forms.is_valid():
			forms.save()
			forms = DocumentCreationForm()


			return redirect('/add-document')

	return render(request, 'add_document.html' , context)





def ViewDocument(request):
	queryset = Document.objects.all()
	search_query = request.GET.get('search' , '')
	if search_query:
		queryset = Document.objects.filter(student__name__icontains = search_query)

	context ={
	"queryset":queryset,
	"search_query":search_query
	}

	return render(request , 'list_document.html' , context)



def EditDocument(request , pk):
	msg =""
	queryset = Document.objects.get(id = pk)
	form = DocumentUpdateForm(instance = queryset)
	if request.method =="POST":
		form =DocumentUpdateForm(request.POST , instance = queryset)
		if form.is_valid():
			form.save()
			return redirect('/list-document')

	context ={
	'form':form,
	'msg':msg,
	}	
	return render(request , 'edit_document.html' , context)
def DeleteDocument(request , pk):
	queryset = Document.objects.get(id =pk)
	if request.method == "POST":
		queryset.delete()
		return redirect ("/list-document")
	context ={}
	return render(request , "delete_document.html" , context)


 # 	document = DocumentCreationForm(instance = pk)

# documents views end

def AddPayment(request):

	forms = PaymentCreateForm()
	message =""
	if request.method  == "POST":
		forms = PaymentCreateForm(request.POST or None)
		if forms.is_valid():
			payment = forms.save() # save the form and get the saved instance
            # update remaining_amount with course_amount
			course_amount = forms.cleaned_data['course_amount']
			payment.remaining_amount = float(course_amount)
			print("post method calling")
			try:
				payment.save()
				# messages.success(request, "Payment added successfully.")
				return redirect('/list-payment')
			except IntegrityError:
				message = "IntegrityError"
		else:
			message = "payment Already Added"

	else:
		messsage ="data is not posted due to  incomplete input"
		# print("not post method call") 


	context ={
	'form':forms,
	'msg':message
	}

	return render(request , 'payment.html' , context)

def EditPayment(request , pk):
	msg =""
	queryset = Payment.objects.get(id = pk)
	form = PaymentUpdateForm(instance = queryset)
	if request.method =="POST":
		form =PaymentUpdateForm(request.POST , instance = queryset)
		if form.is_valid():
			form.save()
			return redirect('/list-payment')

	context ={
	'form':form,
	'msg':msg,
	}	
	return render(request , 'edit_payment.html' , context)





def ViewPayment(request):
	queryset = Payment.objects.all()
	search_query = request.GET.get('search', '')
	if search_query:
		queryset = Payment.objects.filter(student__name__icontains=search_query)
	else:
		queryset = Payment.objects.all()

	context ={
	"queryset":queryset,
	"search_query":search_query
	}

	return render(request, 'payment_list.html' , context)




# bill_no = 1100 
# def generate_bill_no():
#     global bill_no
#     bill_no += 1
#     return bill_no

from django.core.cache import cache

def generate_bill_no():
    # Check if the 'bill_no' key exists in the cache
    if 'bill_no' in cache:
        bill_no = cache.get('bill_no')
    else:
        bill_no = 1100  # Initial bill number
        cache.set('bill_no', bill_no)

    # Increment the bill number and update it in the cache
    next_bill_no = bill_no + 1
    cache.set('bill_no', next_bill_no)

    return next_bill_no

def  PaymentTransaction(request):
	forms = PaymentTransactionForm()
	msg =""
	payment = Payment.objects.all()
	if payment:
		if request.method == 'POST':
			student_id = request.POST.get('student')
			course_id = request.POST.get('course')
			pay_amount = request.POST.get('pay_amount')
			payments = Payment.objects.filter(student_id=student_id, course_id=course_id)
			due_amount = 0.0
			if payments:
				for instance in payments:
					due_amount = instance.remaining_amount
					payment_id = instance.id
				print(payments)
				if due_amount >= float(pay_amount):
					instance.remaining_amount = float(due_amount) - float(pay_amount)
					instance.save()
					bill_no = generate_bill_no()
					course_name = instance.course
					student_name = instance.student
					payment = Payment_History(
	       										bill_no=bill_no,
	        									student_name=student_name,
	        									course_name=course_name,
	        									paid_amount=pay_amount
	        									)
					payment.save()

					return redirect('/list-payment')
				else:
					msg ="your pay amount is greater than remaining amount"
			# payment = Payment.objects.filter(stutdent_id =pk)
			else:
				msg= "payment is not added with this name and course "
	else:
		msg ="payment is not added to any student's course"

	context ={
	
	'form':forms ,
	"msg":msg
	}

	return render(request , "payment_transaction.html" , context)


def PaymentReport(request):
	queryset = Payment_History.objects.all()
	context ={
	"queryset":queryset,
	}
	return render(request , "payment_report.html", context)