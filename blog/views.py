from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required  
from .models import Post
from .forms import PostForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts')  # Redirect to home page after successful login
        else:
            # Handle invalid login
            return render(request, 'blog/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'blog/login.html')

@login_required  # Apply login_required decorator to restrict access to authenticated users only
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})

        
@login_required        
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

@login_required
def user_dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    for post in user_posts:
        print(post.post_id)  
    return render(request, 'blog/user_dashboard.html', {'user_posts': user_posts})



def delete_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)  # Use post_id instead of pk
    if request.method == 'POST':
        post.delete()
    return redirect('blog/home.html')
