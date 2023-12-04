from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Remedy, MateriaMedica


class IndexView(generic.ListView):
    template_name = "homeo/index.html"
    context_object_name = "remedy_list"

    def get_queryset(self):
        """Return the list of remedies"""
        return Remedy.objects.select_related().all()


class RemedyView(generic.DetailView):
    model = Remedy
    template_name = "homeo/remedy.html"


class MateriaView(generic.DetailView):
    model = MateriaMedica
    template_name = "homeo/materia.html"


def remedy(request, remedy_id):
    r = get_object_or_404(Remedy, pk=remedy_id)
    return render(request, "homeo/remedy.html", {"remedy": r})


def materia(request, materia_id):
    m = get_object_or_404(MateriaMedica, pk=materia_id)
    return render(request, "homeo/materia.html", {"materia": m})


