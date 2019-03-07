# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsBannerCentral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='adsBannerCentral/')),
                ('url', models.URLField(default='www.directoriodime.com.mx', null=True)),
            ],
            options={
                'verbose_name': 'Banner Principal Home',
                'verbose_name_plural': 'Banner Principal Home',
            },
        ),
        migrations.CreateModel(
            name='AdsBannerLateral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='adsBannerLateral/')),
                ('url', models.URLField(default='www.directoriodime.com.mx', null=True)),
            ],
            options={
                'verbose_name': 'Banner Lateral Home',
                'verbose_name_plural': 'Banners Laterales Home',
            },
        ),
        migrations.CreateModel(
            name='AdsRandomLateral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='adsRandomLaterial/')),
                ('url', models.URLField(default='www.directoriodime.com.mx', null=True)),
            ],
            options={
                'verbose_name': 'Banner Aleatorio Lateral',
                'verbose_name_plural': 'Banners Aleatorios Laterales',
            },
        ),
        migrations.CreateModel(
            name='AdsRandomSuperior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='adsRandomSuperior/')),
                ('url', models.URLField(default='www.directoriodime.com.mx', null=True)),
            ],
            options={
                'verbose_name': 'Banner Aleatorio Central',
                'verbose_name_plural': 'Banners Aleatorios Centrales',
            },
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('icono', models.ImageField(null=True, upload_to='iconosClasificaciones/', blank=True)),
                ('categoria', models.ForeignKey(default=1, to='dir.Categoria')),
            ],
            options={
                'verbose_name': 'Clasificacion',
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compania', models.CharField(max_length=100)),
                ('nombre', models.CharField(default='Nombre(s) del Contacto', max_length=50, blank=True)),
                ('apellido_paterno', models.CharField(default='Apellido Paterno del Contacto', max_length=50, blank=True)),
                ('apellido_materno', models.CharField(default='Apellido Materno del Contacto', max_length=50, blank=True)),
                ('cargo', models.CharField(default='Cargo que ejerce el Contacto en la Company', max_length=100, blank=True)),
                ('tipo_oficina', models.CharField(default=2, max_length=1, choices=[('1', 'Casa'), ('2', 'Oficina')])),
                ('calle', models.CharField(default='Calle y Numero', max_length=100)),
                ('localidad', models.CharField(default='Colonia o Fraccionamiento', max_length=100)),
                ('ciudad', models.CharField(default='Ciudad', max_length=100)),
                ('estado', models.CharField(default='NON', max_length=3, choices=[('AGS', 'Aguascalientes'), ('BCN', 'Baja California Norte'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHP', 'Chiapas'), ('CHI', 'Chihuahua'), ('DIF', 'Ciudad de M\xe9xico'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('GTO', 'Guanajuato'), ('GRO', 'Guerrero'), ('HGO', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'M\xe9xico'), ('MIC', 'Michoac\xe1n'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo Le\xf3n'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QRO', 'Quer\xe9taro'), ('ROO', 'Quintana Roo'), ('SLP', 'San Luis Potos\xed'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLX', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucat\xe1n'), ('ZAC', 'Zacatecas'), ('NON', 'Selecciona un Estado')])),
                ('codigo_postal', models.CharField(default='C.P. #####', max_length=15)),
                ('telefono', models.CharField(default='55 5555 555', max_length=100)),
                ('email', models.EmailField(default='correo@empresa.com.mx', max_length=254, blank=True)),
                ('pagina_web', models.URLField(default='www.empresa.com.mx', blank=True)),
                ('mayorista', models.BooleanField(default=False)),
                ('premium', models.BooleanField(default=False)),
                ('logo', models.ImageField(null=True, upload_to='logosPremium/', blank=True)),
                ('categorias', models.ManyToManyField(to='dir.Categoria', blank=True)),
                ('clasificaciones', models.ManyToManyField(to='dir.Clasificacion', blank=True)),
            ],
            options={
                'verbose_name': 'COMPA\xd1\xcdA',
                'verbose_name_plural': 'COMPA\xd1\xcdAS',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, null=True, blank=True)),
                ('lugar', models.CharField(max_length=140, null=True, blank=True)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_final', models.DateField(null=True, blank=True)),
                ('url', models.URLField(default='www.directoriodime.com.mx', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, null=True, blank=True)),
                ('comercializadores', models.ManyToManyField(to='dir.Compania')),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, null=True, blank=True)),
                ('calle', models.CharField(default='Calle y Numero', max_length=100)),
                ('localidad', models.CharField(default='Colonia o Fraccionamiento', max_length=100)),
                ('ciudad', models.CharField(default='Ciudad', max_length=100)),
                ('estado', models.CharField(default='NON', max_length=3, choices=[('AGS', 'Aguascalientes'), ('BCN', 'Baja California Norte'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHP', 'Chiapas'), ('CHI', 'Chihuahua'), ('DIF', 'Ciudad de M\xe9xico'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('GTO', 'Guanajuato'), ('GRO', 'Guerrero'), ('HGO', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'M\xe9xico'), ('MIC', 'Michoac\xe1n'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo Le\xf3n'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QRO', 'Quer\xe9taro'), ('ROO', 'Quintana Roo'), ('SLP', 'San Luis Potos\xed'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLX', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucat\xe1n'), ('ZAC', 'Zacatecas'), ('NON', 'Selecciona un Estado')])),
                ('codigo_postal', models.CharField(default='C.P. #####', max_length=15)),
                ('telefono', models.CharField(default='55 5555 555', max_length=100)),
                ('email', models.EmailField(default='correo@empresa.com.mx', max_length=254, blank=True)),
                ('pagina_web', models.URLField(default='www.empresa.com.mx', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Organizaciones',
            },
        ),
        migrations.AddField(
            model_name='artista',
            name='contacto',
            field=models.ManyToManyField(to='dir.Compania'),
        ),
        migrations.AddField(
            model_name='adsrandomsuperior',
            name='categoria',
            field=models.ForeignKey(to='dir.Categoria'),
        ),
        migrations.AddField(
            model_name='adsrandomsuperior',
            name='clasificaciones',
            field=models.ManyToManyField(to='dir.Clasificacion', blank=True),
        ),
        migrations.AddField(
            model_name='adsrandomlateral',
            name='categoria',
            field=models.ForeignKey(to='dir.Categoria'),
        ),
        migrations.AddField(
            model_name='adsrandomlateral',
            name='clasificaciones',
            field=models.ManyToManyField(to='dir.Clasificacion', blank=True),
        ),
    ]
