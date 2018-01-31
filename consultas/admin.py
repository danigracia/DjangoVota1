from django.contrib import admin

from .models import Pregunta, Respuesta, Voto, Invitacion

class CrearRespuestas(admin.StackedInline):
    model = Respuesta
    extra = 3


class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pregunta']}),
        ('Fecha inicio y final', {'fields': ['fecha_ini','fecha_fin']}),
    ]
    inlines = [CrearRespuestas]




admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
admin.site.register(Voto)
admin.site.register(Invitacion)