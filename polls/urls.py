from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/', views.api_data, name='api_data')
]