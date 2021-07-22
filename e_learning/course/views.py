from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Video,Student,Author
from .forms import videoform,authorform,studentform,Submit_valid_proofs
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()


# Page for Guest User and whenever User opens on another tab depending upon the type of user , page should open
def visit(req):

	if req.user.is_anonymous:
		obj=Video.objects.all()
		return render(req,'visit.html',{'data':obj})
	elif req.user.is_superuser:
		return render(req,'admin_html_page.html')
	elif req.user.role=='Student':
		return redirect("s_home")
	else:
		return redirect("a_home")

# Sign Up Form For Student
def s_signup(req):
	if req.method=='POST':
		form=studentform(req.POST)
		print("I am in the POST form")
		if form.is_valid():
			print("Form is valid")
			r=form.save(commit=False)
			r.save()
			obj=Student.objects.create(user_id=int(r.uid()))
			obj.s_name=r.first_name + " "+r.last_name;
			obj.email=r.email
			obj.save()
			print("Student name is ",obj.s_name)
			username = req.POST['username']
			password1 = req.POST['password1']
			user = authenticate(req, username=username, password=password1)
			login(req,user)
			return redirect("s_home")

		else:
			print("Form is invalid")
			print(form.errors)
			return render(req,'reg_student.html',{'data':form})
			# print(form)
			# print("Invalid Form")
			# print(form.errors)
			# return render(request, 'app/add.html',{'form':form})

	form=studentform()
	return render(req,'reg_student.html',{'data':form})

# Sign Up Form For Teacher
def a_signup(req):

	if req.method=='POST':
		form=authorform(req.POST,req.FILES)
		if form.is_valid():
			r=form.save(commit=False)
			r.role="Teacher"
			r.save()
			obj=Author.objects.create(user_id=int(r.uid()))
			obj.a_name=r.first_name + " "+r.last_name;
			obj.email=r.email
			# obj.a_qualification=r.a_qualification
			obj.a_qualification=req.POST['a_qualification']
			obj.proof=req.FILES['proof']
			obj.save()
			print("Author qualification is ",obj.a_qualification)
			username = req.POST['username']
			password1 = req.POST['password1']
			user = authenticate(req, username=username, password=password1)
			login(req,user)
			return redirect("a_home")
		
		print("Form is invalid")
		print(form.errors)
		return render(req,'reg_student.html',{'data':form})
		# print("Form is invalid")
		# print(form.errors)
	else:
		form=authorform()
		return render(req,'reg_author.html',{'data':form})

# Login Page for both Student,Teacher and Admin

def login_view(req):

	if req.method=='POST':
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(req, username=username, password=password)
		if user is not None:
			login(req,user)
			print("User role is ",user.role)
			
			if user.is_superuser:
				print("Hi Admin")
				return redirect(admin_home)

			elif user.role == "Student":
				if 'next_url' in req.POST:
					return redirect(req.POST.get('next_url'))
				return redirect(s_home)
			else:
				if 'next_url' in req.POST:
					return redirect(req.POST.get('next_url'))
				return redirect(a_home)
		else:
			print("Please Sign Up")
			return redirect("visit")
	else:
		form=AuthenticationForm()
		return render(req,'login.html',{'form':form})

# Home Page For Admin

def admin_home(req):
	return render(req,'admin_html_page.html')




# Home Page for Teacher
def a_home(req):
	data=Author.objects.get(user_id=req.user.id)
	obj3=Video.objects.all().filter(author_id=req.user.id)
	return render(req,'a_home.html',{'data':data,'data1':obj3})


# Home Page for Student
# Footer is properly applied to Student Home 
def s_home(req):
	data=Student.objects.get(user_id=req.user.id)
	obj=Video.objects.all()


	# obj1=Author.objects.get(user=req.user.id)
	# print("The name of Author is ",obj1.a_name)
	# obj2=obj1.video_set.all()
	# print("The courses of that author is ")
	# # print(obj2)


	print("The name of student is ",data)
	return render(req,'s_home.html',{'data':data,'obj':obj})


# Enrolling the student for the course

def s_enroll(req,vid):


	# print("The id of video is ",vid," and the id of student is ",req.user.id)

	student=Student.objects.get(user_id=req.user.id)


	video=Video.objects.get(id=vid)


	video.enrolled_student.add(student)

	# print(video.enrolled_student.all())



	return render(req,'student_enrolled.html',{'data':video})






# Page for playing Course

@login_required
def play(req,id):
	obj=Video.objects.get(id=id)
	return render(req,'play.html',{'data':obj})


# Page for adding a new Course 

@login_required(login_url='/a_login')
def add(req):
	print("Username of author is ",req.user.username)
	if req.method == 'POST':
		form = videoform(req.POST,req.FILES)
		if form.is_valid():
			obj=form.save(commit=False)
			print(obj)
			obj.author_id=req.user.id
			obj.save()
			return redirect('a_home')
	else:
		form = videoform()

	return render(req, 'addvideo.html', {'obj': form})



def s_learning(req):

	student=Student.objects.get(user_id=req.user.id)
	# print(student)
	
	video = Video.objects.filter(enrolled_student__s_name=student)
	
	# print(video)

	return render(req,'s_learning.html',{'data':video})




# See the status of author in Admin Page

def admin_teacher_status(req):
	obj=Author.objects.filter(status="Pending")
	print(obj)
	return render(req,"admin_teacher_status.html",{'data':obj})

# See the status of course

def admin_course_status(req):
	obj=Video.objects.filter(status="Pending")
	return render(req,"admin_course_status.html",{'data':obj})





# Changing the status of Teacher

def accept_teacher_status(req,aid):
	obj=Author.objects.get(user_id=aid)
	obj.status="Verified"
	obj.save()
	return redirect(admin_teacher_status)


def reject_teacher_status(req,aid):
	obj=Author.objects.get(user_id=aid)
	obj.status="Rejected"
	obj.save()
	return redirect(admin_teacher_status)


# Changing the status of Teacher


def accept_course_status(req,vid):
	obj=Video.objects.get(id=vid)
	obj.status="Verified"
	obj.save()
	return redirect(admin_course_status)



def reject_course_status(req,vid):
	obj=Video.objects.get(id=vid)
	obj.status="Rejected"
	obj.save()
	return redirect(admin_course_status)



def submit_valid_proof(req,aid):
	if req.method=='POST':
		obj1=Author.objects.get(user_id=aid)
		form = Submit_valid_proofs(req.POST,req.FILES)
		if form.is_valid():
			f1=form.save(commit=False)
			print(f1)
			obj1.status="Pending"
			obj1.proof=req.FILES['proof']
			obj1.save()
			return redirect('a_home')
		
	obj=Submit_valid_proofs()
	return render(req,'submit_valid_proofs.html',{'data':obj})



def video_rejected(req,vid):
	obj=Video.objects.get(id=vid)
	if req.method == 'POST':
		form = videoform(req.POST,req.FILES)
		if form.is_valid():
			obj1=form.save(commit=False)
			print(obj1)
			obj.title=req.POST['title']
			obj.status="Pending"
			obj.video=req.FILES['video']
			obj.save()
			# obj.author_id=req.user.id
			# obj.save()
			return redirect('a_home')
		else:
			print("form has Errors")
			print(form.errors)
			return render(req,"change_video_content.html",{'obj1':form,'data':obj})
	
	form = videoform(instance=obj)
	print(obj)
	return render(req,'change_video_content.html',{'obj1':form,'data':obj})



def remove_video(req,vid):
	obj=Video.objects.get(id=vid)
	obj.delete()
	return redirect(a_home)

# def stuents_enrolled(req,cid):
# 	obj=Video.objects.get(id=cid)
	



# #View the list of courses of that particular author

# def a_course(req):
# 	obj1=Author.objects.get(user=req.user.id)
# 	print("The name of Author is ",obj1.a_name)
# 	obj2=obj1.video_set.all()
# 	print("The courses of that author is ")
# 	# print(obj2)
# 	obj3=Video.objects.all().filter(author_id=req.user.id)
# 	print(obj3)
# 	return render(req,'a_course.html',{'data':obj3})
