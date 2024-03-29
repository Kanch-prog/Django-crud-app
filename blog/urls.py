from django.contrib.auth import views as auth_views
from django.urls import path
from .views import delete_post
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  
    path('', views.home, name='posts'),
    path('about/', views.about, name='about'),
    path('post/create/', views.create_post, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'), 
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]
