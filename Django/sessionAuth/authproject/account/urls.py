from django.urls import path
from . import views # get_csrf, login_view, logout_view, protected_view

urlpatterns = [
    path('get-csrf/', views.get_csrf, name='Get Csrf'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('protected/', views.protected_view, name='Protected'),
]