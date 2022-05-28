from django.urls import path
from unicodedata import name
from. import views
from django.contrib.auth import views as auth_views
app_name='accounts'
urlpatterns = [
    path('',views.Base.as_view(),name='base'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]