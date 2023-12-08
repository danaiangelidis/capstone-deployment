from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from views import Home

urlpatterns = [
    #path("", Home(request)),
    path("admin/", admin.site.urls)
]