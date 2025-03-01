from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('login/', views.my_login, name="my-login"),
    path('register/', views.my_register, name="my-register"),
    path('logout/', views.my_logout, name="my-logout"), 
    path('dashboard/', views.dashboard, name="dashboard"),
    #=========================================================================
    #=========================FRONT END===============================
    #=========================================================================
    path('blog/', views.front_blog,name="front-blog"), 
    path('blog-list/<int:blog_id>/', views.blog_list, name='blog-list'),
    path('front-portofolio/', views.front_portofolio, name='front-portofolio'),
    path('front-skill/', views.front_skill, name='front-skill'),
     path('skills/<str:category_name>/',views.skill_view, name='skill-list'),
    path('front-certi/,', views.front_certi, name='front-certi'),
    path('front-course/,', views.front_course, name='front-course'),

    #=========================================================================
    #=========================CRUD WORK EXP===============================
    #=========================================================================
    path('create-workexp/', views.create_workexp, name="create-workexp"),
    path('view-workexp/', views.view_workexp, name="view-workexp"),
    path('update-workexp/<str:pk>', views.update_workexp, name="update-workexp"),
    path('delete-workexp/<str:pk>', views.delete_workexp, name="delete-workexp"),

    # =============================================================================
    # =======================PORTOFOLIO ROUTE======================================
    # =============================================================================
    path('create-porto/', views.create_porto, name="create-porto"), 
    path('view-porto/', views.view_porto, name="view-porto"), 
    path('update-porto/<str:pk>', views.update_porto, name="update-porto"), 
    path('delete-porto/<str:pk>', views.delete_porto, name="delete-porto"), 

     # =============================================================================
    # =======================CERTIFICATE======================================
    # =============================================================================
    path('create-certi/', views.create_certi, name="create-certi"), 
    path('view-certi/', views.view_certi, name="view-certi"), 
    path('update-certi/<str:pk>', views.update_certi, name="update-certi"), 
    path('delete-certi/<str:pk>', views.delete_certi, name="delete-certi"), 
     # =============================================================================
    # =======================COURSE======================================
    # =============================================================================
    path('create-course/', views.create_course, name="create-course"), 
    path('view-course/', views.view_course, name="view-course"), 
    path('update-course/<str:pk>', views.update_course, name="update-course"), 
    path('delete-course/<str:pk>', views.delete_course, name="delete-course"), 

    # =============================================================================
    # =======================SKILL======================================
    # =============================================================================
    path('create-skill/', views.create_skill, name="create-skill"), 
    path('view-skill/', views.view_skill, name="view-skill"), 
    path('update-skill/<str:pk>', views.update_skill, name="update-skill"), 
    path('delete-skill/<str:pk>', views.delete_skill, name="delete-skill"), 

        # =============================================================================
    # =======================BLOG======================================
    # =============================================================================
    path('create-blog/', views.create_blog, name="create-blog"), 
    path('view-blog/', views.view_blog, name="view-blog"), 
    path('update-blog/<str:pk>', views.update_blog, name="update-blog"), 
    path('delete-blog/<str:pk>', views.delete_blog, name="delete-blog"), 
]
