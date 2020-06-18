from django.urls import path

from .views import GalleryView

app_name = 'gallery_app'





urlpatterns = [

    path('Austerllungen/', GalleryView.as_view(), name='gallery_page'),


]
