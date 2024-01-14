
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('letter/', include('letter.urls')),
    path('peoples/', include('peoples.urls')),
    path('gallery/', include('gallery.urls')),
]
