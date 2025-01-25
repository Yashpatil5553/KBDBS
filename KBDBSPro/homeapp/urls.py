from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for index view
    path('home/', views.HomePage, name='home'),  # URL for HomePage view
    path('login/', views.LoginPage, name='login'),  # URL for login page
    path('logout/', views.user_logout, name='logout'),  
    path('noaccess/', views.noaccesspg, name='noaccess'),  
    path('cmapp/', include('cmapp.urls')),
    path('KRISapp/', include('KRISapp.urls')),
]