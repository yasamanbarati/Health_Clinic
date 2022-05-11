from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='logIn_page'),
    path('logout/', views.LogoutView.as_view(), name='logOut_page'),
    path('forget_pass/', views.ForgetPassView.as_view(), name='forget_pass_page'),
    path('Reset_pass/<activeaccount>/', views.ReesetPassView.as_view(), name='reset_pass_page'),
    path('activate_account/<activeCode>/', views.ActiveAccountView.as_view(), name='activate_account'),
    # path('Complete_register/', views.CompleteRegisterView.as_view(), name='CompleteRegister')
    path('Complete_register/', views.EditUserProfilePage.as_view(), name='CompleteRegister')
]
