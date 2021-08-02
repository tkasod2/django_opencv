from django.urls import path
from . import views

from django.conf import settings
#setting.py 땡겨오는 import
from django.conf.urls.static import static


app_name = 'opencv_webapp'


urlpatterns = [
    path('',views.first_view, name='first_view'), #127.0.0.1:8000/
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#                              /media/,     media의 folder 위치
