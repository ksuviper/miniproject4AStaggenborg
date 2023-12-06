from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "homeo"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.RemedyView.as_view(), name="remedy"),
    path("<int:pk>/materia/", views.MateriaView.as_view(), name="materia"),
]



