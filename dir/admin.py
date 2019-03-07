# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from models import Compania, Clasificacion, Categoria, AdsBannerCentral, AdsBannerLateral, Artista, Organizacion, Evento, Marca, AdsRandomLateral, AdsRandomSuperior
from django.utils.encoding import python_2_unicode_compatible

from django.contrib import admin

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
admin.autodiscover()


# Register your models here.
# ___________________________
class CompaniaAdmin(admin.ModelAdmin):
    list_display = [
        'compania',
        'estado',
        'mayorista',
    ]
    list_filter = [
        'estado',
        'categorias'
    ]
    search_fields = ('compania',)


admin.site.register(Compania, CompaniaAdmin)


class ClasificacionAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'slug',
        'categoria',
    ]
    list_filter = [
        'categoria',
    ]
    search_fields = ('nombre',)


admin.site.register(Clasificacion, ClasificacionAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'slug',
    ]
    search_fields = ('nombre',)
    # prepopulated_fields = {'slug': ('nombre',)}


admin.site.register(Categoria, CategoriaAdmin)


class AdsBannerCentralAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
    ]
    search_fields = ('titulo',)
    # prepopulated_fields = {'slug': ('nombre',)}


admin.site.register(AdsBannerCentral, AdsBannerCentralAdmin)


class AdsBannerLateralAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
    ]
    search_fields = ('titulo',)
    # prepopulated_fields = {'slug': ('nombre',)}


admin.site.register(AdsBannerLateral, AdsBannerLateralAdmin)


class AdsRandomLateralAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
    ]
    search_fields = ('titulo',)
    # prepopulated_fields = {'slug': ('nombre',)}


admin.site.register(AdsRandomLateral, AdsRandomLateralAdmin)


class AdsRandomSuperiorAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
    ]
    search_fields = ('titulo',)
    # prepopulated_fields = {'slug': ('nombre',)}


admin.site.register(AdsRandomSuperior, AdsRandomSuperiorAdmin)


class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'fecha_inicio',
        'fecha_final',
    ]
    search_fields = ('nombre',)


admin.site.register(Evento, EventoAdmin)


class ArtistaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]
    search_fields = ('nombre',)
    raw_id_fields = ('contacto',)


admin.site.register(Artista, ArtistaAdmin)


class MarcaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]
    search_fields = ('nombre',)
    raw_id_fields = ('comercializadores',)


admin.site.register(Marca, MarcaAdmin)


class OrganizacionAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'estado',
        'pagina_web',
    ]
    search_fields = ('nombre',)


admin.site.register(Organizacion, OrganizacionAdmin)

