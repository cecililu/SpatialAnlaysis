from django.contrib import admin
from django.urls import path,include

from utils.views import BufferPolygonIntersectionView,BufferPolygonView,BuildingdataPost,BuildingInfo

urlpatterns = [
    
    path("building/", BufferPolygonIntersectionView.as_view()),
    path('buffer/',BufferPolygonView.as_view()),
    path('newdata/',BuildingdataPost.as_view()),
    path('buildinginfo/',BuildingInfo.as_view())

    # path('addbuildingdata/',CreateBuildingAttributeInfo.as_view())
    
]
