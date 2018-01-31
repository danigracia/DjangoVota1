from django.db import models

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=200)
    fecha_ini = models.DateTimeField('Fecha inicio')
    fecha_fin = models.DateTimeField('Fecha final')
    def __str__(self):
            return self.pregunta


class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=200)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    num_votos = models.IntegerField(default=0)
    def __str__(self):
            return self.respuesta

class Voto(models.Model):
    id_voto = models.AutoField(primary_key=True)
    id_respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    id_usuario = models.CharField(max_length=10)
    def __str__(self):
            return self.id_respuesta


class Invitacion(models.Model):
    id_invitacion = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=70)
    id_pregunta = models.CharField(max_length=10)
    def __str__(self):
            return self.email

