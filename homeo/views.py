from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Remedy, RemedyPotency, RemedyMateriaMedica, Potency, MateriaMedica


class IndexView(generic.ListView):
    template_name = "homeo/index.html"
    context_object_name = "latest_question_list"


class RemedyView(generic.DetailView):
    model = Remedy
    template_name = "homeo/remedy.html"


class MateriaView(generic.DetailView):
    model = MateriaMedica
    template_name = "homeo/materia.html"



