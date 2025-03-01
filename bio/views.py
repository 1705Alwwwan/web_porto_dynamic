from django.shortcuts import render, redirect, get_object_or_404
from .forms  import CreateUserForm, LoginForm, WorkExpForm, PortofolioForm, CertificateForm, CourseForm, SkillForm, BlogForm
from django.contrib.auth.models import auth, User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PengalamanKerja, Portofolio, Certificate, Course, Skill, Blog, KindSkill

def home (request):
    return render(request, "bio/index.html")

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        
    context = {'LoginForm':form}
    return render (request, 'login/login.html', context)

def my_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    
    context = {'RegisterForm' : form}
    return render (request, 'register/register.html', context)

def my_logout(request):
    auth.logout(request)
    return redirect('')

@login_required(login_url='my-login')
def dashboard (request):
    return render (request, "bio/dashboard.html")


#====================================================================================
#===================================WORK EXPERIENCES==================================
#====================================================================================
@login_required(login_url='my-login')
def create_workexp(request):
    form = WorkExpForm()
    if request.method == 'POST':
        form = WorkExpForm(request.POST, request.FILES)
        if form.is_valid(): 
            upgrade_data = form.save(commit=False)
            upgrade_data.user = request.user

            upgrade_data.save()
            return redirect('view-workexp')
        
    context = {'CreateWorkExpForm':form}
    return render (request, 'workexp/create-workexp.html',context)


@login_required(login_url='my-login')
def view_workexp(request):
    work_exp = PengalamanKerja.objects.all().order_by('-start_date')

    context = {'work_exp':work_exp}
    return render(request, 'workexp/view-workexp.html', context)

@login_required(login_url='my-login')
def update_workexp(request, pk):
    try:
        work_exp = PengalamanKerja.objects.get(id=pk)
    except:
        return redirect('view-workexp')
    
    form = WorkExpForm(instance=work_exp)
    if request.method == 'POST':
        form = WorkExpForm(request.POST, request.FILES , instance=work_exp)
        if form.is_valid():
            form.save()
            return redirect('view-workexp')
        
    context = {'UpdateWorkExp':form}
    return render (request, 'workexp/update-workexp.html', context)

@login_required(login_url='my-login')
def delete_workexp(request, pk):
    try:
        work_exp = PengalamanKerja.objects.get(id=pk)
    except:
        return redirect('view-workexp')
    
    if request.method == 'POST':
        work_exp.delete() 
        return redirect('view-workexp')
    return render (request, 'workexp/delete-workexp.html') 


# =================================================================================
# ================PORTOFOLIO FORM==================================================
# =================================================================================
@login_required(login_url='my_login')
def create_porto(request):
    form = PortofolioForm
    if request.method == 'POST':
        form = PortofolioForm(request.POST, request.FILES)
        if form.is_valid():
            upgrade_data = form.save(commit=False)
            upgrade_data.user = request.user
            upgrade_data.save()
            return redirect('view-porto')

    context = {'CreatePortoForm' : form}
    return render(request, 'portofolio/create-portofolio.html', context)

@login_required(login_url='my_login')
def view_porto(request):
    portofolio = Portofolio.objects.all().order_by('-date_posted')  # Urutkan dari terbaru ke terlama
    context = {'PortofolioData':portofolio}
    return render(request, 'portofolio/view-portofolio.html', context)

@login_required(login_url='my_login')
def update_porto(request,pk):
    try:
        DataPortofolio = Portofolio.objects.get(id=pk)
    except:
        return redirect ('view-porto')
    
    form = PortofolioForm(instance=DataPortofolio)
    if request.method=="POST":
        form = PortofolioForm(request.POST,request.FILES, instance=DataPortofolio)
        if form.is_valid():
            form.save()
            return redirect('view-porto')
        

    context = {'DataPortofolioAll':form}
    return render(request, 'portofolio/update-portofolio.html', context)

@login_required(login_url='my_login')
def delete_porto(requeset, pk):
    try:
        DataPortofolio = Portofolio.objects.get(id=pk)
    except:
        return redirect ('view-porto')
    
    if requeset.method =="POST":
        DataPortofolio.delete()
        return redirect('view-porto')
    return render(requeset, 'portofolio/delete-portofolio.html')

# =================================================================================
# ================CERTIFICAATE==================================================
# =================================================================================
@login_required(login_url='my_login')
def create_certi(request):
    form = CertificateForm()
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            upgrade_data = form.save(commit=False)
            upgrade_data.user = request.user
            upgrade_data.save()
            return redirect('view-certi')

    context = {'CertificateForm' : form}
    return render(request, 'certificate/create-certi.html', context)

@login_required(login_url='my_login')
def view_certi(request):
    certificate = Certificate.objects.all().order_by('-date_posted')  # Urutkan dari terbaru ke terlama
    context = {'DataCerti':certificate}
    return render(request, 'certificate/view-certi.html', context)

@login_required(login_url='my_login')
def update_certi(request,pk):
    try:
        DataCertificate = Certificate.objects.get(id=pk)
    except:
        return redirect ('view-certi')
    
    form = CertificateForm(instance=DataCertificate)
    if request.method=="POST":
        form = CertificateForm(request.POST,request.FILES, instance=DataCertificate)
        if form.is_valid():
            form.save()
            return redirect('view-certi')
        

    context = {'UpdateDataCerti':form}
    return render(request, 'certificate/update-certi.html', context)

@login_required(login_url='my_login')
def delete_certi(requeset, pk):
    try:
        DataCerti = Certificate.objects.get(id=pk)
    except:
        return redirect ('view-porto')
    
    if requeset.method =="POST":
        DataCerti.delete()
        return redirect('view-certi')
    return render(requeset, 'certificate/delete-certi.html')

# =================================================================================
# ================COURSE SESSION==================================================
# =================================================================================

@login_required(login_url='my_login')
def create_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            upgrade_data = form.save(commit=False)
            upgrade_data.user = request.user
            upgrade_data.save()
            return redirect('view-course')

    context = {'CourseForm' : form}
    return render(request, 'course/create-course.html', context)

@login_required(login_url='my_login')
def view_course(request):
    coursedata = Course.objects.all().order_by('-do_date')  # Urutkan dari terbaru ke terlama
    context = {'DataCourse':coursedata}
    return render(request, 'course/view-course.html', context) 

@login_required(login_url='my_login')
def update_course(request,pk):
    try:
        DataCourse = Course.objects.get(id=pk)
    except:
        return redirect ('view-course')
    
    form = CourseForm(instance=DataCourse)
    if request.method=="POST":
        form = CourseForm(request.POST,request.FILES, instance=DataCourse)
        if form.is_valid():
            form.save()
            return redirect('view-course')
        

    context = {'UpdateDataCourse':form}
    return render(request, 'course/update-course.html', context) 

@login_required(login_url='my_login')
def delete_course(requeset, pk):
    try:
        DataCourse = Course.objects.get(id=pk)
    except:
        return redirect ('view-course')
    
    if requeset.method =="POST":
        DataCourse.delete()
        return redirect('view-course')
    return render(requeset, 'course/delete-course.html')


# =================================================================================
# ================Skill Session==================================================
# =================================================================================
@login_required(login_url='my_login')
def create_skill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            upgrade_data = form.save(commit=False)
            upgrade_data.user = request.user
            upgrade_data.save()
            return redirect('view-skill')

    context = {'SkillForm' : form}
    return render(request, 'skill/create-skill.html', context)

@login_required(login_url='my_login')
def view_skill(request):
    skilldata = Skill.objects.all().order_by('-date_posted')  # Urutkan dari terbaru ke terlama
    context = {'DataSkill':skilldata}
    return render(request, 'skill/view-skill.html', context) 

@login_required(login_url='my_login')
def update_skill(request,pk):
    try:
        dataskill = Skill.objects.get(id=pk)
    except:
        return redirect ('view-skill')
    
    form = SkillForm(instance=dataskill)
    if request.method=="POST":
        form = SkillForm(request.POST, instance=dataskill)
        if form.is_valid():
            form.save()
            return redirect('view-skill')
        

    context = {'UpdateDataSkill':form}
    return render(request, 'skill/update-skill.html', context) 


@login_required(login_url='my_login')
def delete_skill(requeset, pk):
    try:
        DataSkill = Skill.objects.get(id=pk)
    except:
        return redirect ('view-skill')
    
    if requeset.method =="POST":
        DataSkill.delete()
        return redirect('view-skill')
    return render(requeset, 'skill/delete-skill.html') 

# =================================================================================
# ================BLOG Session==================================================
# =================================================================================
@login_required(login_url='my_login')
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            upgrade_data = form.save(commit=False)
            upgrade_data.user = request.user
            upgrade_data.save()
            return redirect('view-blog')

    context = {'BlogFormData' : form}
    return render(request, 'blog/create-blog.html', context)

@login_required(login_url='my_login')
def view_blog(request):
    DataBlog = Blog.objects.all().order_by('-date_posted')  # Urutkan dari terbaru ke terlama
    context = {'DataBlog':DataBlog}
    return render(request, 'blog/view-blog.html', context) 


@login_required(login_url='my_login')
def update_blog (request,pk):
    try:
        datablog = Blog.objects.get(id=pk)
    except:
        return redirect ('view-blog')
    
    form = BlogForm(instance=datablog)
    if request.method=="POST":
        form = BlogForm(request.POST, instance=datablog)
        if form.is_valid():
            form.save()
            return redirect('view-blog')
        

    context = {'UpdateDataBlog':form}
    return render(request, 'blog/update-blog.html', context) 


@login_required(login_url='my_login')
def delete_blog(requeset, pk):
    try:
        DataBlog = Blog.objects.get(id=pk)
    except:
        return redirect ('view-blog')
    
    if requeset.method =="POST":
        DataBlog.delete()
        return redirect('view-blog')
    return render(requeset, 'blog/delete-blog.html') 

# =================================================================================
# ================FRONT-END==================================================
# =================================================================================

def front_blog(request):
    blogs = Blog.objects.all().order_by('-date_posted') 
    context = {'blogs': blogs}
    return render(request, 'bio/blog.html', context)

def blog_list(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)  # Mengambil blog berdasarkan ID
    context = {'blog': blog}
    return render(request,'bio/blog_table.html', context)

def front_portofolio (request):
    portofolio = Portofolio.objects.all().order_by('date_posted')
    context= {'portofolio':portofolio}
    return render(request, 'bio/portofolio.html', context)

def front_skill (request):
    return render(request, 'bio/skill.html')

def skill_view(request, category_name):
    # Ambil objek KindSkill berdasarkan kategori
    selected_kind = KindSkill.objects.filter(skill_category=category_name).first()

    # Ambil semua skill yang sesuai dengan kategori
    skills = Skill.objects.filter(kind_skill=selected_kind).order_by('skill_name')

    return render(request, 'bio/skill_table.html', {
        'skills': skills,
        'category_name': category_name
    })
    

def front_certi (request):
    DataCertificate = Certificate.objects.all().order_by('date_posted')
    context = {'datacerti':DataCertificate}
    return render(request, 'bio/certification.html', context)

def front_course (request):
    DataCourse = Course.objects.all().order_by('date_posted')
    context = {'datacourse':DataCourse}
    return render(request, 'bio/course.html', context)




