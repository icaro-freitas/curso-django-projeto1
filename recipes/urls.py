from django.urls import path
from recipes.views import home

# return HTTP Response


urlpatterns = [
    path('', home),
]
