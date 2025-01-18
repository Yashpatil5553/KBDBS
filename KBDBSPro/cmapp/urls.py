from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cmhome/', views.CMHome_page, name='cmhome'),
    path('process/', views.sheetprocess, name='process'),
    path('update/', views.updatebalance, name='update'),
    path('voucher/', views.vouchergen, name='voucher'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)