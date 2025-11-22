from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

# Create User Registration Form this is used for Singup
class UserRegistrationFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


# Create Login Form use to login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Create Post Form to Edit the post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

# Create Comment Form to save comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]