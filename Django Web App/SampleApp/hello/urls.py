from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("predict", views.predict, name="predict"),
    path("<str:value>", views.show_input, name="show_input")
]