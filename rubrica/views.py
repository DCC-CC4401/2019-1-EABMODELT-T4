from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Rubric


# Create your views here.

def index(request):
    return render(request, 'rubrica/index.html', context={})


def createRubric(request):
    # TODO crear contexto vacío
    if request.method == 'POST':
        # TODO crear/parsear json, agregar modelo a la bd, mostrar pagina de "logrado"
        pass
    return render(request, 'rubrica/crear.html', context={})


def seeRubric(request, rubric_id=0):
    # TODO crear contexto a partir de rubric_id
    # rubric = get_object_or_404(Rubric, pk=rubric_id)
    return render(request, 'rubrica/ver.html', context={})


def modifyRubric(request, rubric_id=0):
    # TODO crear contexto a partir de rubric_id
    # rubric = get_object_or_404(Rubric, pk=rubric_id)
    if request.method == 'POST':
        # TODO crear/parsear json, agregar modelo a la bd, mostrar pagina de "logrado"
        pass
    return render(request, 'rubrica/ver.html', context={})
