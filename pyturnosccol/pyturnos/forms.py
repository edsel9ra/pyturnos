from collections.abc import Mapping
from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, Form
from django.forms.utils import ErrorList
from .models import Registros, TurnosProgramados, Turnos, Justificaciones, Empleados
from django import forms
#from django_select2 import forms as s2forms
#from dynamic_forms import DynamicField, DynamicFormMixin

# Formulario para los registros
class FormRegistro(forms.ModelForm):
    class Meta:
        model = Registros
        fields = ['empleado', 'turno_programado', 'fecha_registro_entrada', 'hora_registro_entrada', 'fecha_registro_salida', 'hora_registro_salida']
        widgets = {
            'empleado': forms.Select(attrs={'class': 'select2 form-control'}),
            'turno_programado': forms.Select(attrs={'class': 'form-control select2'}),
            'fecha_registro_entrada': forms.NumberInput(attrs={'type': 'date'}),
            'hora_registro_entrada': forms.NumberInput(attrs={'type': 'time'}),
            'fecha_registro_salida': forms.NumberInput(attrs={'type': 'date'}),
            'hora_registro_salida': forms.NumberInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormRegistro, self).__init__(*args, **kwargs)
        self.fields['turno_programado'].queryset = TurnosProgramados.objects.none()

        if 'empleado' in self.data:
            empleado_id = self.data.get('empleado')
            self.fields['turno_programado'].queryset = TurnosProgramados.objects.filter(empleado__id_empleado=empleado_id)
        elif self.instance.pk:
            self.fields['turno_programado'].queryset = self.instance.empleado.turnoprogramado_set.all()

# Formulario para los empleados


class FormEmpleado(ModelForm):
    class Meta:
        model = Empleados
        fields = ['id_empleado', 'nombre_empleado', 'apellido_paterno_empleado',
                  'apellido_materno_empleado', 'fecha_nacimiento_empleado', 'sexo_empleado',
                  'telefono_empleado', 'email_empleado', 'departamento_empleado',
                  'centro_costo', 'estado', 'fecha_ingreso_empleado', 'fecha_baja_empleado',
                  'fecha_reingreso_empleado']
        widgets = {
            'sexo_empleado': forms.Select(attrs={'class': 'select2'}),
            'departamento_empleado': forms.Select(attrs={'class': 'select2'}),
            'centro_costo': forms.Select(attrs={'class': 'select2'}),
            'estado': forms.Select(attrs={'class': 'select2'}),
            'fecha_nacimiento_empleado': forms.NumberInput(attrs={'type': 'date'}),
            'fecha_ingreso_empleado': forms.NumberInput(attrs={'type': 'date'}),
            'fecha_baja_empleado': forms.NumberInput(attrs={'type': 'date'}),
            'fecha_reingreso_empleado': forms.NumberInput(attrs={'type': 'date'}),
        }


# Formulario para los turnos
class FormTurnos(ModelForm):
    class Meta:
        model = Turnos
        fields = ['id_turno', 'hora_inicial', 'hora_final', 'tipo_turno']
        widgets = {
            'tipo_turno': forms.Select(attrs={'class': 'select2'}),
            'hora_inicial': forms.NumberInput(attrs={'type': 'time'}),
            'hora_final': forms.NumberInput(attrs={'type': 'time'}),
        }

# Formulario para las justificaciones


class FormJustificaciones(ModelForm):
    class Meta:
        model = Justificaciones
        fields = ['id_justificacion', 'descripcion_justificacion']

# Formulario para las programaciones


class FormTurnosProgramados(ModelForm):
    class Meta:
        model = TurnosProgramados
        fields = ['empleado', 'turno', 'fecha_turno', 'justificacion']
        widgets = {
            'turno': forms.Select(attrs={'class': 'select2 form-control'}),
            'empleado': forms.Select(attrs={'class': 'select2 form-control'}),
            'justificacion': forms.Select(attrs={'class': 'select2 form-control'}),
            'fecha_turno': forms.NumberInput(attrs={'type': 'date'}),
        }

# TXT


class UploadTextForm(forms.Form):
    text_file = forms.FileField(label='Archivo TXT')
