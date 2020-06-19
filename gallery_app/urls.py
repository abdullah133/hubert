from django.urls import path

from .views import GalleryView

app_name = 'gallery_app'





urlpatterns = [

    path('Ausstellungen/', GalleryView.as_view(), name='gallery_page'),


]
