from flask import Flask, render_template, url_for, flash, redirect
from flaskweb.forms import RegistrationForm, LoginForm
from flaskweb.models import User, Post
from flaskweb import app

posts = [
    {
        'post_id': 1,
        'title':'Building Minimal Web Interfaces',
        'text':'Learn how to design clean, fast, and user-friendly interfaces without unnecessary complexity.',
        'publish_date':'Jan 5, 2026'
    },
    {
        'post_id': 2,
        'title':'Why Simplicity Matters in Design',
        'text':'Simplicity improves usability, accessibility, and performance across all devices.',
        'publish_date':'Dec 28, 2025'
    },
    {
        'post_id': 3,
        'title':'Getting Started with Modern HTML',
        'text':'A beginner-friendly guide to writing semantic, modern, and maintainable HTML.',
        'publish_date':'Dec 18, 2025'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts, heading='This Is HomePage')

@app.route("/about-us")
def about():
    return render_template('about.html')

@app.route("/blog")
def post():
    return render_template('blog.html')

@app.route("/contact-us")
def contact():
    return render_template('contact.html')

@app.route("/register", methods=['GET','POST'])
def registerView():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash (f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login")
def loginView():
    loginform = LoginForm()
    return render_template('login.html', form=loginform)