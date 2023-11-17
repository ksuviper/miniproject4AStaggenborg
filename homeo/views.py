from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Remedy, RemedyPotency, RemedyMateriaMedica, Potency, MateriaMedica


class IndexView(generic.ListView):
    model = Remedy
    template_name = "homeo/index.html"
    context_object_name = "remedy_list"

    # def get_queryset(self):
    #     """Return the list of remedies"""
    #     return Remedy.objects.select_related().all().order_by("name")


class RemedyView(LoginRequiredMixin, generic.DetailView):
    login_url = '/admin/login/'
    model = Remedy
    template_name = "homeo/remedy.html"


class MateriaView(LoginRequiredMixin, generic.DetailView):
    login_url = '/admin/login/'
    model = MateriaMedica
    template_name = "homeo/materia.html"



