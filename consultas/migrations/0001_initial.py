# Generated by Django 2.0.1 on 2018-02-01 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitacion',
            fields=[
                ('id_invitacion', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=70)),
                ('id_pregunta', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=200)),
                ('fecha_ini', models.DateTimeField(verbose_name='Fecha inicio')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fecha final')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.CharField(max_length=200)),
                ('num_votos', models.IntegerField(default=0)),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id_voto', models.AutoField(primary_key=True, serialize=False)),
                ('id_usuario', models.CharField(max_length=10)),
                ('id_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Respuesta')),
            ],
        ),
    ]
