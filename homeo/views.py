from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Remedy, MateriaMedica


class RemedyView(generic.DetailView):
    """remedy view"""
    model = Remedy
    template_name = "homeo/remedy.html"


class MateriaView(generic.DetailView):
    """materia medica view"""
    model = MateriaMedica
    template_name = "homeo/materia.html"


def index(request):
    """index page"""
    """check to see if the search box was used."""
    if request.GET.get("query") is not None:
        q = request.GET.get("query")
        r = Remedy.objects.select_related().filter(name__startswith=q)
    else:
        q = ""
        r = Remedy.objects.select_related().all()

    return render(request, "homeo/index.html", {"remedy_list": r, "query": q})


def remedy(request, remedy_id):
    """lookup remedy by id"""
    r = get_object_or_404(Remedy, pk=remedy_id)
    return render(request, "homeo/remedy.html", {"remedy": r})


def materia(request, materia_id):
    """lookup materia media by id"""
    m = get_object_or_404(MateriaMedica, pk=materia_id)
    return render(request, "homeo/materia.html", {"materia": m})


