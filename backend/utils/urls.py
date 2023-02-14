from django.contrib import admin
from django.urls import path,include

from utils.views import *

urlpatterns = [
    path("building/", BufferPolygonIntersectionView.as_view()),
    
    path('buffer/',BufferPolygonView.as_view())
]
