from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationFrom, LoginForm, PostForm
from .models import Post

#----------------------------------------------------------------------------
# Authentication Logic
#----------------------------------------------------------------------------
# Registration View (Create new User)
def register_view(request):
    if request.method == 'POST' :
        form = UserRegistrationFrom(request.POST)
        # Validate the from
        if form.is_valid():
            form.save() # --> User Created
            messages.success(request,"Account Created Successfully")
            return redirect('login')
        
    else:
        form = UserRegistrationFrom()

    return render(request,'register.html', {'form': form})

# Login View (Login a user & create session)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Validate
        if form.is_valid():
            username = form.cleaned_data['username'] # --> Take user name
            password = form.cleaned_data['password'] # --> Take user password

            user = authenticate(request, username=username, password=password) # Authenticate

            if user is not None:
                login(request,user) # --> Session id Created
                return redirect('home')
            else:
                messages.error(request, "Invalid Username & Password")

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#----------------------------------------------------------------------------
# Blog Logic
#----------------------------------------------------------------------------
# Home Blog Listing Page
def home_view(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'home.html', {'posts': posts})

# Blog Details Page
def details_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'details.html', {'post': post})

# Create Blog Post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   # --> set Loggin user as Author
            post.save()
            messages.success(request, "Post Created Successfully")
            return redirect('home')
        
    else:
        form = PostForm()

    return render(request, 'createpost.html', {'form': form})

# Edit Blog Post
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Only Author can edit
    if request.user != post.author:
        messages.error(request,"Your are not allowed to edit this post")
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited successfully")
            return redirect('details', slug=post.slug)
        
    else:
        form = PostForm(instance=post)

    return render(request, 'editpost.html', {'form': form})

# Delete Post 
@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user != post.author:
        messages.error(request, "You are not allowed to Delete this post")
        return redirect('home')
    
    post.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('home')




