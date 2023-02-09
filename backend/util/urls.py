from .views import BufferPolygonView
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    # ... other URLs ...
    path('buffer_polygon/', BufferPolygonView.as_view(), name='buffer_polygon'),
]