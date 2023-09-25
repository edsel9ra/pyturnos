from django.contrib import admin
from .models import Departamentos, GruposEmpleados, CentrosCostos, Empleados, Turnos, Justificaciones, TurnosProgramados, Registros

#Register your models here.
admin.site.register(Departamentos)
admin.site.register(GruposEmpleados)
admin.site.register(CentrosCostos)
#admin.site.register(Departamentos) --> Futura implementación
admin.site.register(Empleados)
admin.site.register(Turnos)
admin.site.register(Justificaciones)
admin.site.register(TurnosProgramados)
admin.site.register(Registros)