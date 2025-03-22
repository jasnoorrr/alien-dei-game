from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cover_page, name='cover'),
    path('country/<str:country_name>/', views.country_view, name='country'),
]
