from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('KRIShome/', views.KRISHome_page, name='KRIShome'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)