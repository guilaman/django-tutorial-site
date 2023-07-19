from django.contrib import admin
from django.urls import include, path

urlpatterns = [
        path("my_polls/", include("my_polls.urls")),
        path("admin/", admin.site.urls),
        ]
