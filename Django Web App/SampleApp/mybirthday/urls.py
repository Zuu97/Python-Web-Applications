from django.urls import path
from . import views

urlpatterns = [
    path("<str:month>/<str:day>", views.check_birth, name="check_birth")
]