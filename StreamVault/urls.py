
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'StreamVault Admin Page' #name of admin panel
admin.site.site_title = 'StreamVault | Admin' #tab name
admin.site.index_title = 'Welcome to the admin console. ©2024 StreamVault Inc.' #desc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('accounts/',include('accounts.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
