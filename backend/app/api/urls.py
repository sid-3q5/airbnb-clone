from django.urls import path
from app.api.views import ListAV,DetailAV

urlpatterns = [
    path('list/', ListAV.as_view(),name='list'),
    path('<int:pk>/',DetailAV.as_view(),name='movie_detail'),
]

