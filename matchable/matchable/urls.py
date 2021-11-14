from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include
from index.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name = 'main'),
    path('index/', include('index.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)