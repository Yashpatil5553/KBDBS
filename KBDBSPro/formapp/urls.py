from django.urls import path, include
from . import views

urlpatterns = [
    path('formhome/',views.formhome_page, name='formhome'),
    path('formpg/', views.form_page, name='formpg'),
]
