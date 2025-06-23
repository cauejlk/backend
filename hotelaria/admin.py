from django.contrib import admin

from .models import (
   Hospede,
   Quartos,
   Cargos,
   Funcionarios,
   Reserva,
   Servicos,
   Reserva_Servicos,
   Turno,
   Tipo_quarto
)


admin.site.register(Hospede)
admin.site.register(Tipo_quarto)
admin.site.register(Turno)
admin.site.register(Cargos)
admin.site.register(Quartos)
admin.site.register(Funcionarios)
admin.site.register(Reserva)
admin.site.register(Servicos)
admin.site.register(Reserva_Servicos)

