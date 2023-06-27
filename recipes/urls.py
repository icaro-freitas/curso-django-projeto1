from django.urls import path
from recipes.views import contato, home, sobre

# return HTTP Response


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
