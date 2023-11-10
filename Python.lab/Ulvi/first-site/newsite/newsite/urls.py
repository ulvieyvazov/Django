from django.contrib import admin
from django.urls import path, include
from test.views import pageNotFound

urlpatterns=[
   path("admin/",admin.site.urls),
   path('', include("test.urls")),
]

handler404=pageNotFound