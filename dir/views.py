import random

from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.template import loader
from django.http import HttpResponse
from django.views.generic.base import View
from django.db.models import Q
from dir.models import *


# Create your views here.
# __________________________________________
# Index
# __________________________________________
def index(request):
    categorias = Categoria.objects.all()
    clasificaciones = Clasificacion.objects.all()
    bannerCentral = AdsBannerCentral.objects.all()
    estados = ESTADO_CHOICES
    bannerLateral1 = AdsBannerLateral.objects.get(id=1)
    bannerLateral2 = AdsBannerLateral.objects.get(id=2)

    context_dict = {
        'categorias': categorias,
        'clasificaciones': clasificaciones,
        'estados': estados,
        'bannerCentral': bannerCentral,
        'bannerLateral1': bannerLateral1,
        'bannerLateral2': bannerLateral2,
    }
    return render(request, 'dir/index.html', context_dict)



def about(request):
    categorias = Categoria.objects.all()
    clasificaciones = Clasificacion.objects.all()
    estados = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'clasificaciones': clasificaciones,
        'estados': estados,
    }
    return render(request, 'dir/about.html', context_dict)


CASE_SQL = '(' \
           'case when estado="AGS" ' \
           'then 1 when estado="AGS" ' \
           'then 2 when estado="BCN" ' \
           'then 3 when estado="BCS" ' \
           'then 4 when estado="CAM" ' \
           'then 5 when estado="CHP" ' \
           'then 6 when estado="CHI" ' \
           'then 7 when estado="DIF" ' \
           'then 8 when estado="COA" ' \
           'then 9 when estado="COL" ' \
           'then 10 when estado="AGS" ' \
           'then 11 when estado="DUR" ' \
           'then 12 when estado="GTO" ' \
           'then 13 when estado="GRO" ' \
           'then 14 when estado="HGO" ' \
           'then 15 when estado="JAL" ' \
           'then 16 when estado="MEX" ' \
           'then 17 when estado="MIC" ' \
           'then 18 when estado="MOR" ' \
           'then 19 when estado="NLE" ' \
           'then 20 when estado="OAX" ' \
           'then 21 when estado="PUE" ' \
           'then 22 when estado="QRO" ' \
           'then 23 when estado="ROO" ' \
           'then 24 when estado="SLP" ' \
           'then 25 when estado="SIN" ' \
           'then 26 when estado="SON" ' \
           'then 27 when estado="TAB" ' \
           'then 28 when estado="TAM" ' \
           'then 29 when estado="TLX" ' \
           'then 30 when estado="VER" ' \
           'then 31 when estado="YUC" ' \
           'then 32 when estado="ZAC" ' \
           ')'


# __________________________________________
# categoria
# __________________________________________
def vista_categoria(request, slug_categoria):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'False': False,
    }

    query = request.GET.get("q")

    try:
        categoria = Categoria.objects.get(slug=slug_categoria)
        companias = Compania.objects.filter(categorias=categoria).order_by('estado', 'compania')
        # companias_by_estado = companias.order_by('compania')
        clasificaciones = Clasificacion.objects.filter(categoria=categoria)
        addLateral = AdsRandomLateral.objects.filter(categoria=categoria)
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.filter(categoria=categoria)
        randomAddsSuperior = random.choice(addSuperior)
        if query:
            companias = Compania.objects.filter(compania__icontains=query)
        context_dict['categoria'] = categoria
        context_dict['companias'] = companias
        context_dict['clasificaciones'] = clasificaciones
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Categoria.DoesNotExist:
        addLateral = AdsRandomLateral.objects.filter(categoria=categoria)
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.filter(categoria=categoria)
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['categoria'] = None
        context_dict['companias'] = None
        context_dict['clasificaciones'] = None
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list

    return render(request, 'dir/categoria.html', context_dict)


# __________________________________________
# clasificacion
# __________________________________________
def vista_clasificacion(request, slug_clasificacion):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'False': False,
    }

    query = request.GET.get("q")

    try:
        clasificacion = Clasificacion.objects.get(slug=slug_clasificacion)
        companias = Compania.objects.filter(clasificaciones=clasificacion).order_by('estado')
        addLateral = AdsRandomLateral.objects.filter(clasificaciones=clasificacion)
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.filter(clasificaciones=clasificacion)
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['companias'] = companias
        context_dict['clasificacion'] = clasificacion
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Clasificacion.DoesNotExist:
        addLateral = AdsRandomLateral.objects.filter(clasificaciones=clasificacion)
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.filter(clasificaciones=clasificacion)
        context_dict['categoria'] = None
        context_dict['companias'] = None
        context_dict['clasificacion'] = None
        context_dict['clasificaciones'] = None
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list

    return render(request, 'dir/clasificacion.html', context_dict)


# __________________________________________
# busqueda
# __________________________________________
class SearchSubmitView(View):
    template = 'dir/search-submit.html'
    response_message = 'Resultados de Busqueda:'

    def post(self, request):
        template = loader.get_template(self.template)
        query = request.POST.get('search', '')

        companias = Compania.objects.filter(compania__icontains=query)
        categorias = Categoria.objects.all()
        clasificaciones_list = Clasificacion.objects.all()
        estados_list = ESTADO_CHOICES
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)

        context = {'title': self.response_message, 'query': query, 'companias': companias,
                   'categorias': categorias, 'clasificaciones_list': clasificaciones_list,
                   'estados_list': estados_list, 'randomAddLateral1': randomAddLateral1, 'randomAddLateral2': randomAddLateral2,
                   'randomAddsSuperior': randomAddsSuperior}

        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')


# __________________________________________
# busqueda
# __________________________________________
def SearchSubmitAdvanceView(request):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES
    addLateral = AdsRandomLateral.objects.all()
    randomAddLateral1 = random.choice(addLateral)
    randomAddLateral2 = random.choice(addLateral)
    addSuperior = AdsRandomSuperior.objects.all()
    randomAddsSuperior = random.choice(addSuperior)
    context_dict = {
        'categorias': categorias,
    }

    clasificacion_id = request.POST.get('selectClasificacion')
    estado = request.POST.get('selectEstado')

    try:
        clasificacion = Clasificacion.objects.get(id=clasificacion_id)
        companias = Compania.objects.filter(
            Q(clasificaciones=clasificacion) &
            Q(estado=estado)
        )
        context_dict['companias'] = companias
        context_dict['clasificacion'] = clasificacion
        context_dict['companias'] = companias
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Clasificacion.DoesNotExist:
        context_dict['categoria'] = None
        context_dict['companias'] = None
        context_dict['clasificacion'] = None
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    return render(request, 'dir/busqueda.html', context_dict)


# __________________________________________
# marca
# __________________________________________
def vista_marca(request):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'False': False,
    }
    try:
        marcas = Marca.objects.all()
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['marcas'] = marcas
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Marca.DoesNotExist:
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['marcas'] = None
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list

    return render(request, 'dir/marcas.html', context_dict)


# __________________________________________
# artista
# __________________________________________
def vista_artista(request):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'False': False,
    }
    try:
        artistas = Artista.objects.all()
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['artistas'] = artistas
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Marca.DoesNotExist:
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['artistas'] = None
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list

    return render(request, 'dir/artistas.html', context_dict)


# __________________________________________
# organizaciones
# __________________________________________
def vista_organizacion(request):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'False': False,
    }
    try:
        organizaciones = Organizacion.objects.all()
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['organizaciones'] = organizaciones
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Marca.DoesNotExist:
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['organizaciones'] = None
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list

    return render(request, 'dir/organizaciones.html', context_dict)


# __________________________________________
# evento
# __________________________________________
def vista_evento(request):
    categorias = Categoria.objects.all()
    clasificaciones_list = Clasificacion.objects.all()
    estados_list = ESTADO_CHOICES

    context_dict = {
        'categorias': categorias,
        'False': False,
    }
    try:
        eventos = Evento.objects.all()
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['eventos'] = eventos
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior

    except Marca.DoesNotExist:
        addLateral = AdsRandomLateral.objects.all()
        randomAddLateral1 = random.choice(addLateral)
        randomAddLateral2 = random.choice(addLateral)
        addSuperior = AdsRandomSuperior.objects.all()
        randomAddsSuperior = random.choice(addSuperior)
        context_dict['eventos'] = None
        context_dict['randomAddLateral2'] = randomAddLateral2
        context_dict['randomAddLateral1'] = randomAddLateral1
        context_dict['randomAddSuperior'] = randomAddsSuperior
        context_dict['clasificaciones_list'] = clasificaciones_list
        context_dict['estados_list'] = estados_list

    return render(request, 'dir/eventos.html', context_dict)

