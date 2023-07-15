from django.urls import path

from . import views

# return HTTP Response


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
