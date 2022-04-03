from django.urls import path 
from photo_album.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from . import views


urlpatterns = [
        path('', views.gallery, name='gallery'),
        path('add/', views.addPhoto, name='add'),
        path('photo/<str:pk>/', views.viewPhoto, name='photo')
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)