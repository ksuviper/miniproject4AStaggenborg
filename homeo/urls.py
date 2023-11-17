from django.urls import path

from . import views

app_name = "homeo"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.RemedyView.as_view(), name="remedy"),
    path("<int:pk>/edit/", views.RemedyEdit.as_view(), name="edit_remedy"),
    path("<int:pk>/materia/", views.MateriaView.as_view(), name="materia"),
]
