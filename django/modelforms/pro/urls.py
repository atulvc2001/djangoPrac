"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from aoo1 import views
from app2 import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("insert/", views.insert),
    path("read/", views.read),
    path("delete/<pk>", views.delete),
    path("update/<pk>", views.update),
    path("in/", v.insert),
    path("up/<pk>", v.update),
    path("de/<pk>", v.delete),
    path("rd/", v.read),
    path("inin/", v.insertt.as_view()),
    path("upup/<pk>",v.updatee.as_view()),
    path("deldel/<pk>",v.deletet.as_view()),
    path("rdrd/<pk>",v.rdrd.as_view())

]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
