# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.template import defaultfilters
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse

from django.db import models

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.
# _________________________________
# categoria
# _________________________________
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = defaultfilters.slugify(self.nombre)
            super(Categoria, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


# _________________________________
# clasificacion
# _________________________________
class Clasificacion(models.Model):
    nombre = models.CharField(max_length=50, unique=False)
    categoria = models.ForeignKey(Categoria, default=1)
    slug = models.SlugField(unique=True)
    icono = models.ImageField(upload_to='iconosClasificaciones/', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = defaultfilters.slugify(self.nombre + self.parent)
    #         super(Categoria, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Clasificacion'
        verbose_name_plural = 'Clasificaciones'

    def __str__(self):
        return self.nombre


ESTADO_CHOICES = (
    (u'AGS', u'Aguascalientes'),
    (u'BCN', u'Baja California Norte'),
    (u'BCS', u'Baja California Sur'),
    (u'CAM', u'Campeche'),
    (u'CHP', u'Chiapas'),
    (u'CHI', u'Chihuahua'),
    (u'DIF', u'Ciudad de México'),
    (u'COA', u'Coahuila'),
    (u'COL', u'Colima'),
    (u'DUR', u'Durango'),
    (u'GTO', u'Guanajuato'),
    (u'GRO', u'Guerrero'),
    (u'HGO', u'Hidalgo'),
    (u'JAL', u'Jalisco'),
    (u'MEX', u'México'),
    (u'MIC', u'Michoacán'),
    (u'MOR', u'Morelos'),
    (u'NAY', u'Nayarit'),
    (u'NLE', u'Nuevo León'),
    (u'OAX', u'Oaxaca'),
    (u'PUE', u'Puebla'),
    (u'QRO', u'Querétaro'),
    (u'ROO', u'Quintana Roo'),
    (u'SLP', u'San Luis Potosí'),
    (u'SIN', u'Sinaloa'),
    (u'SON', u'Sonora'),
    (u'TAB', u'Tabasco'),
    (u'TAM', u'Tamaulipas'),
    (u'TLX', u'Tlaxcala'),
    (u'VER', u'Veracruz'),
    (u'YUC', u'Yucatán'),
    (u'ZAC', u'Zacatecas'),
    (u'NON', u'Selecciona un Estado'),
)


# _________________________________
# Compania
# _________________________________
@python_2_unicode_compatible
class Compania(models.Model):
    compania = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50, default="Nombre(s) del Contacto", blank=True)
    apellido_paterno = models.CharField(max_length=50, default="Apellido Paterno del Contacto", blank=True)
    apellido_materno = models.CharField(max_length=50, default="Apellido Materno del Contacto", blank=True)
    cargo = models.CharField(max_length=100, default="Cargo que ejerce el Contacto en la Company", blank=True)
    OFICINA_CHOICES = (
        (u'1', u'Casa'),
        (u'2', u'Oficina'),
    )
    tipo_oficina = models.CharField(choices=OFICINA_CHOICES, default=2, max_length=1)
    calle = models.CharField(max_length=100, default="Calle y Numero")
    localidad = models.CharField(max_length=100, default="Colonia o Fraccionamiento")
    ciudad = models.CharField(max_length=100, default="Ciudad")
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=3, default="NON")
    codigo_postal = models.CharField(max_length=15, default="C.P. #####")
    telefono = models.CharField(max_length=100, default="55 5555 555")
    email = models.EmailField(default="correo@empresa.com.mx", blank=True)
    pagina_web = models.URLField(default="www.empresa.com.mx", blank=True)
    categorias = models.ManyToManyField(Categoria, blank=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    # categorias y clasificaciones
    # audio = models.ManyToManyField(Audio, blank=True)
    # video = models.ManyToManyField(Video, blank=True)
    # iluminacion = models.ManyToManyField(Iluminacion, blank=True)
    # escenarios = models.ManyToManyField(Escenarios, blank=True)
    # instrumentosMusicales = models.ManyToManyField(Instrumentos, blank=True)
    # oficinasProduccion = models.ManyToManyField(Oficinas, blank=True)
    # centrosEspectaculos = models.ManyToManyField(Centros, blank=True)
    # talento = models.ManyToManyField(Talento, blank=True)
    # escuelas = models.ManyToManyField(Escuelas, blank=True)
    # dj = models.ManyToManyField(Dj, blank=True)
    # varios = models.ManyToManyField(Varios, blank=True)
    mayorista = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='logosPremium/', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = defaultfilters.slugify(self.nombre)
    #         super(Compania, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'COMPAÑÍA'
        verbose_name_plural = 'COMPAÑÍAS'

    def __str__(self):
        return self.compania


# ____________________
# Marcas
# ____________________
class Marca(models.Model):
    nombre = models.CharField(max_length=140, null=True, blank=True)
    comercializadores = models.ManyToManyField(Compania)

    def __str__(self):
        return self.nombre


# ____________________
# Artistas
# ____________________
class Artista(models.Model):
    nombre = models.CharField(max_length=140, null=True, blank=True)
    contacto = models.ManyToManyField(Compania)

    def __str__(self):
        return self.nombre


# ____________________
# Eventos
# ____________________
class Evento(models.Model):
    nombre = models.CharField(max_length=140, null=True, blank=True)
    lugar = models.CharField(max_length=140, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, default='www.directoriodime.com.mx')

    def __str__(self):
        return self.nombre


# ____________________
# Organizaciones
# ____________________
class Organizacion(models.Model):
    nombre = models.CharField(max_length=140, null=True, blank=True)
    calle = models.CharField(max_length=100, default="Calle y Numero")
    localidad = models.CharField(max_length=100, default="Colonia o Fraccionamiento")
    ciudad = models.CharField(max_length=100, default="Ciudad")
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=3, default="NON")
    codigo_postal = models.CharField(max_length=15, default="C.P. #####")
    telefono = models.CharField(max_length=100, default="55 5555 555")
    email = models.EmailField(default="correo@empresa.com.mx", blank=True)
    pagina_web = models.URLField(default="www.empresa.com.mx", blank=True)

    class Meta:
        verbose_name_plural = 'Organizaciones'

    def __str__(self):
        return self.nombre


# ____________________
# Ads Fijos
# ____________________
class AdsBannerCentral(models.Model):
    titulo = models.CharField(max_length=140, null=True)
    imagen = models.ImageField(upload_to='adsBannerCentral/', null=True)
    url = models.URLField(null=True, default='www.directoriodime.com.mx')

    class Meta:
        verbose_name = 'Banner Principal Home'
        verbose_name_plural = 'Banner Principal Home'

    def __str__(self):
        return self.titulo


# ____________________
# Ads Fijos
# ____________________
class AdsBannerLateral(models.Model):
    titulo = models.CharField(max_length=140, null=True)
    imagen = models.ImageField(upload_to='adsBannerLateral/', null=True)
    url = models.URLField(null=True, default='www.directoriodime.com.mx')

    class Meta:
        verbose_name = 'Banner Lateral Home'
        verbose_name_plural = 'Banners Laterales Home'

    def __str__(self):
        return self.titulo


# ____________________
# Ads Random
# ____________________
class AdsRandomLateral(models.Model):
    titulo = models.CharField(max_length=140, null=True)
    categoria = models.ForeignKey(Categoria)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    imagen = models.ImageField(upload_to='adsRandomLaterial/', null=True)
    url = models.URLField(null=True, default='www.directoriodime.com.mx')

    class Meta:
        verbose_name = 'Banner Aleatorio Lateral'
        verbose_name_plural = 'Banners Aleatorios Laterales'

    def __str__(self):
        return self.titulo


# ____________________
# Ads Random
# ____________________
class AdsRandomSuperior(models.Model):
    titulo = models.CharField(max_length=140, null=True)
    categoria = models.ForeignKey(Categoria)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    imagen = models.ImageField(upload_to='adsRandomSuperior/', null=True)
    url = models.URLField(null=True, default='www.directoriodime.com.mx')

    class Meta:
        verbose_name = 'Banner Aleatorio Central'
        verbose_name_plural = 'Banners Aleatorios Centrales'

    def __str__(self):
        return self.titulo
