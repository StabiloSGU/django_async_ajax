from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ajax_test import views

app_name = 'ajax_test'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajx/', views.ajx, name='ajx'),
    path('get_filelist/', views.get_filelist, name='get_filelist'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
