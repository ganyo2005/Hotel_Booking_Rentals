from django.urls import path
from .forms import LoginForm
from .views import signup   
from django.contrib.auth import views as auth_view

app_name='account'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='templates/authPages/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),


]
