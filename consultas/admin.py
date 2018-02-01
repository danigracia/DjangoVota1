from django.contrib import admin

from .models import Pregunta, Respuesta, Voto, Invitacion

class CrearRespuestas(admin.StackedInline):
    model = Respuesta
    extra = 3


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['id_pregunta','pregunta', 'propietario', 'fecha_ini', 'fecha_fin']
    fieldsets = [
        (None,               {'fields': ['pregunta']}),
        ('Fecha inicio y final', {'fields': ['fecha_ini','fecha_fin']}),
    ]
    inlines = [CrearRespuestas]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(propietario=request.user)

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['id_respuesta', 'respuesta', 'num_votos', 'id_pregunta']
    fieldsets = [
            (None,               {'fields': ['respuesta','id_pregunta']}),
        ]


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Voto)
admin.site.register(Invitacion)