from django import forms

from .models import Video,Author

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

import django.forms.widgets

from django.contrib.auth import get_user_model
User = get_user_model()

class videoform(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','banner','video']
        widgets={
			
			'title':forms.TextInput(attrs={
				'class':"form-control mt-3",
				'placeholder':"Enter Course Title",
				}),
			'video':forms.FileInput(attrs={
				'class':"mb-3",
				}),

		}

class studentform(UserCreationForm):
	first_name=forms.CharField(label="First name",required=True,widget=forms.TextInput(attrs={'class':"form-control my-3 ",'placeholder':"Enter your first name",}))
	last_name=forms.CharField(label="Last name",required=True,widget=forms.TextInput(attrs={'class':"form-control my-3 ",'placeholder':"Enter your last name",}))
	def __init__(self, *args, **kwargs):		
		super(studentform, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control my-3'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control my-3'})
	class Meta:
		fields=("first_name",'last_name','username','email')
		model = User
		widgets={
			
			'username':forms.TextInput(attrs={
				'class':"form-control mt-3",
				'placeholder':"Enter your username",
				}),
			'email':forms.EmailInput(attrs={
				'class':" form-control my-3",
				'placeholder':"Enter your Email"
				}),

		}

class authorform(UserCreationForm):
	first_name=forms.CharField(label="First name",required=True,widget=forms.TextInput(attrs={'class':"form-control my-3 ",'placeholder':"Enter your first name",}))
	last_name=forms.CharField(label="Last name",required=True,widget=forms.TextInput(attrs={'class':"form-control my-3 ",'placeholder':"Enter your last name",}))
	a_qualification=forms.CharField(label="Your Qualification",required=True,widget=forms.TextInput(attrs={'class':"form-control my-3",'placeholder':"Enter your qualifications",}))
	proof=forms.ImageField()
	def __init__(self, *args, **kwargs):		
		super(authorform, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control my-3'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control my-3 '})
	class Meta:
		fields=("first_name",'last_name','username','email','a_qualification','proof')
		model = User
		widgets={
			
			'username':forms.TextInput(attrs={
				'class':"form-control my-3",
				'placeholder':"Enter your username",
				}),
			'email':forms.EmailInput(attrs={
				'class':" form-control my-3",
				'placeholder':"Enter your Email"
				}),

		}
	
class Submit_valid_proofs(forms.ModelForm):
	class Meta:
		model=Author
		fields=['proof']
		widgets={

		'proof':forms.FileInput(

			attrs={'required': True}

		)

		}

# class Meta:
# 	model = Author
# 	fields = ['a_name','a_qualification','username','password']
    

# class Registrationform(UserCreationForm):
# 	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# 	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# 	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),max_length=100)

# 	def __init__(self, *args, **kwargs):		
# 		super(Registrationform, self).__init__(*args, **kwargs)
# 		for fieldname in ['username', 'password1', 'password2']:
# 			self.fields[fieldname].help_text = None
# 		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
# 		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
# 	class Meta:
# 		model=User
# 		fields=("first_name",'last_name','username','email')
# 		widgets={
			
# 			'username':forms.TextInput(attrs={
# 				'class':"form-control"
# 				}),
# 			'password1':forms.PasswordInput(attrs={
# 				'class':"form-control"
# 				})

# 		}