from django.contrib import admin
from django.urls import include, path
from polls import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('api/', views.api_data, name='api_data')
]