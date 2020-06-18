from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static



admin.site.site_header = "TREEATHLON Admin"
admin.site.index_title = "TREEATHLON Admin Portal"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('', include('about_app.urls')),
    path('', include('gallery_app.urls')),
    path('', include('news_app.urls')),
    path('', include('contact_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
