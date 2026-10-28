from django.contrib import admin
from django.urls import path
from demoapp.views import demo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo, name='demo'),
]
