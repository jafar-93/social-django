from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterAccountView.as_view(), name='user_register'),
    path('login/', views.LoginAccountView.as_view(), name='user_login'),
    path('logout/', views.LogoutAccountView.as_view(), name='user_logout'),

]