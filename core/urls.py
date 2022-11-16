from django.urls import path
from .import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("create/", views.createCard, name="create-card"),
    path("detailed/<str:pk>", views.detailedView, name="detailed"),
]