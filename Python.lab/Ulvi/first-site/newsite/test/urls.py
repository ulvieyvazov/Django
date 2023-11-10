from django.urls import path, re_path
from test import views  

urlpatterns=[
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path("user/<str:name>/<int:age>", views.user),
    re_path(r'^archive/(?P<year>[0-9]{4})/',views.archive),
]
