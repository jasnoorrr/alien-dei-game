from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover_page, name='cover'),
    path('map/', views.map_page, name='map'),
    path('country/<str:country_name>/', views.country_view, name='country'),
    path('reflection/', views.reflection_page, name='reflection'),
]
