from django.urls import path
from . import views
from django.contrib.auth import views as auth_logout

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/', auth_logout.LogoutView.as_view(),name="logout"),
    path('login/', auth_logout.LoginView.as_view(template_name="login.html"),name="login"),
    path('setting/change_password/', auth_logout.PasswordChangeView.as_view(template_name="change_password.html"),name="change_password"),
    path('setting/change_password/done/',auth_logout.PasswordChangeDoneView.as_view(template_name="change_password_done.html"),name='password_change_done'),

]