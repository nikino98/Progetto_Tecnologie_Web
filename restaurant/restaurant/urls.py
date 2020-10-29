"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
import users
from . import views
from .views import homepage
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('offers/', include('offers.urls')),
    # path('users2/', include('users2.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# per le immagini
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
