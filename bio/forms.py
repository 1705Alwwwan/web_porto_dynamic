from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import PengalamanKerja, Portofolio, Certificate, Course, Skill, Blog

class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateUserForm (UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ""  # Menghapus help_text dari semua field

class WorkExpForm(ModelForm):
    class Meta:
        model = PengalamanKerja
        fields = ['job_title', 'company_name','location', 'start_date', 'end_date', 'is_current','image', 'description', ]
        exclude = ['user', 'date_posted', ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PortofolioForm (ModelForm):
    
    class Meta:
        model = Portofolio
        fields = ['title', 'do_date', 'image','description',]
        exclude = ['user', 'date_posted', ]
        widgets = {
            'do_date' : forms.DateInput(attrs={'type':'date'}), 
            'image' : forms.FileInput(attrs={'class':'form-control-file'}), 
        }

class CertificateForm (ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'do_date', 'image','description',]
        exclude = ['user', 'date_posted', ]
        widgets = {
            'do_date' : forms.DateInput(attrs={'type':'date'}), 
            'image' : forms.FileInput(attrs={'class':'form-control-file'}), 
        }

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'do_date','is_current','end_date', 'image','description',]
        exclude = ['user', 'date_posted', ]
        widgets = {
            'do_date' : forms.DateInput(attrs={'type':'date'}), 
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'image' : forms.FileInput(attrs={'class':'form-control-file'}), 
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['kind_skill', 'skill_name',]
        exclude = ['user', 'date_posted',]

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'descripiton', 'image', ]
        

    

        