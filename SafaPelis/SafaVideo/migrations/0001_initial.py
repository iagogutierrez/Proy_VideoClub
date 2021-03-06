# Generated by Django 3.2.9 on 2021-11-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('idPeli', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='Nombre de la Pelicula')),
                ('categoria', models.CharField(max_length=30, verbose_name='Enfoque de la Pelicula')),
                ('fech_alquiler', models.DateField(verbose_name='Fecha Alquiler')),
                ('fech_devol', models.DateField(verbose_name='Fecha Devolucion')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
            },
        ),
    ]
