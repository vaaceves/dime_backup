from django.conf.urls import url
from dir import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^categoria/(?P<slug_categoria>[\w\-]+)/$', views.vista_categoria, name='vista_categoria'),
    url(r'^clasificacion/(?P<slug_clasificacion>[\w\-]+)/$', views.vista_clasificacion, name='vista_clasificacion'),
    url(r'^busqueda/$', views.SearchSubmitView.as_view(), name='search_submit'),
    url(r'^busqueda-adv/$', views.SearchSubmitAdvanceView, name='search_adv'),
    url(r'^marcas/$', views.vista_marca, name='vista_marca'),
    url(r'^artistas/$', views.vista_artista, name='vista_artista'),
    url(r'^eventos/$', views.vista_evento, name='vista_evento'),
    url(r'^organizaciones/$', views.vista_organizacion, name='vista_organizacion'),
    #url(r'^audio/$', views.audio, name='audio'),
    #url(r'^$', views.lista_productos, name='lista_productos'),
    #url(r'^producto/(?P<slug_clasificacion>[\w\-]+)/$', views.lista_por_clasificacion, name='lista_por_clasificacion'),
]