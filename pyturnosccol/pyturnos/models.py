from typing import Iterable, Optional
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, timedelta, datetime

# Modelo de Departamentos
class Departamentos(models.Model):
    id_departamento = models.CharField(primary_key=True, max_length=3)
    nombre_departamento = models.CharField(
        verbose_name="Departamento", max_length=70)
    descripcion_departamento = models.TextField(
        verbose_name="Descripción", blank=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.nombre_departamento

# Modelo de Grupos Empleados
class GruposEmpleados(models.Model):
    id_grupo_emp = models.AutoField(primary_key=True)
    descripcion_grupo = models.CharField(
        verbose_name='Descripcion Grupo Empleados', max_length=50)

    class Meta:
        verbose_name = "Grupo Empleados"
        verbose_name_plural = "Grupos Empleados"

    def __str__(self):
        return self.descripcion_grupo

# Modelo de Centros de Costos
class CentrosCostos(models.Model):
    id_centro = models.CharField(
        verbose_name='ID Centro de Costo', primary_key=True, max_length=8)
    descripcion_centro = models.CharField(
        verbose_name='Descripción Centro de Costos', max_length=50)
    grupo_empleado = models.ForeignKey(
        GruposEmpleados, on_delete=models.CASCADE, verbose_name="Grupo Empleados")

    class Meta:
        verbose_name = "Centro de Costos"
        verbose_name_plural = "Centros de Costos"

    def __str__(self):
        return self.descripcion_centro

# Modelo de Cargos (Para futura implementación)

# Modelo de Empleados(Colaboradores)
class Empleados(models.Model):

    #Implementar modelo SEXOS (Para futura implementación)
    SEXO_CHOICES = {
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('NB', 'No Binario'),
    }

    #Implementar modelo ESTADOS (Para futura implementación)
    ESTADOS_CHOICES = {
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    }

    id_empleado = models.CharField(
        verbose_name="Documento", primary_key=True, max_length=20)
    nombre_empleado = models.CharField(verbose_name="Nombre", max_length=120)
    apellido_paterno_empleado = models.CharField(
        verbose_name="Primer apellido", max_length=70)
    apellido_materno_empleado = models.CharField(
        verbose_name="Segundo Apellido", max_length=70, blank=True)
    fecha_nacimiento_empleado = models.DateField(
        verbose_name="Fecha Nacimiento")
    sexo_empleado = models.CharField(
        verbose_name="Sexo/Genero", max_length=2, choices=SEXO_CHOICES)
    telefono_empleado = models.CharField(
        verbose_name="Teléfono", max_length=11, null=True, blank=True)
    email_empleado = models.EmailField(
        verbose_name="Correo", null=True, blank=True)
    departamento_empleado = models.ForeignKey(
        Departamentos, on_delete=models.CASCADE, verbose_name="Departamento")
    centro_costo = models.ForeignKey(
        CentrosCostos, on_delete=models.CASCADE, verbose_name="Centro de Costos", default=None)
    #cargo (para futura implementación)
    estado = models.CharField(
        verbose_name="Estado Empleado", max_length=1, choices=ESTADOS_CHOICES)
    fecha_ingreso_empleado = models.DateField(verbose_name="Fecha Ingreso")
    fecha_baja_empleado = models.DateField(
        verbose_name="Fecha Salida", null=True, blank=True)
    fecha_reingreso_empleado = models.DateField(
        verbose_name="Fecha Reingreso", null=True, blank=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return '{} {} {}'.format(self.nombre_empleado, self.apellido_paterno_empleado, self.apellido_materno_empleado)

# Modelo de Turnos
class Turnos(models.Model):
    TIPO_TURNO_CHOICES = {
        ('ADM', 'Administrativo'),
        ('AST', 'Asistencial'),
        ('24H', 'Día Completo'),
    }

    id_turno = models.CharField(primary_key=True, max_length=3)
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    tipo_turno = models.CharField(
        verbose_name="Tipo Turno", max_length=3, choices=TIPO_TURNO_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __str__(self):
        return '({}) [{} - {}]'.format(self.id_turno, self.hora_inicial, self.hora_final)

# Modelo de Justificaciones
class Justificaciones(models.Model):
    id_justificacion = models.CharField(
        verbose_name='Código', primary_key=True, max_length=3)
    descripcion_justificacion = models.CharField(
        verbose_name='Descripción', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Justificación"
        verbose_name_plural = "Justificaciones"

    def __str__(self):
        return self.descripcion_justificacion

# Modelo de Turnos Programados
class TurnosProgramados(models.Model):

    id_turno_programado = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(
        Empleados, on_delete=models.CASCADE, verbose_name="Empleado", related_name='turnos_programados')
    turno = models.ForeignKey(
        Turnos, on_delete=models.CASCADE, verbose_name="Turno a Programar")
    fecha_turno = models.DateField(null=True, blank=True)
    justificacion = models.ForeignKey(
        Justificaciones, on_delete=models.CASCADE, verbose_name='Justificación')

    class Meta:
        verbose_name = "Turno Programado"
        verbose_name_plural = "Turnos Programados"
    
    def __str__(self):
        return '{} [Fecha: {}]'.format(self.empleado.id_empleado, self.fecha_turno)

# Modelo de Registros
class Registros(models.Model):
    id_registro = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado")
    turno_programado = models.ForeignKey(TurnosProgramados, on_delete=models.CASCADE, verbose_name="Turno Programado")
    turno = models.ForeignKey(Turnos, on_delete=models.SET_NULL, verbose_name="Turno", null=True, blank=True)
    justificacion = models.ForeignKey(Justificaciones, on_delete=models.SET_NULL, verbose_name="Justificacion", null=True, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)
    fecha_registro_entrada = models.DateField(null=True, blank=True)
    hora_registro_entrada = models.TimeField(null=True, blank=True)
    fecha_registro_salida = models.DateField(null=True, blank=True)
    hora_registro_salida = models.TimeField(null=True, blank=True)
    # Campos para las observaciones segun los datos del registro
    obs_marcacion = models.CharField(verbose_name="Marcación", max_length=50, blank=True, null=True)
    obs_entrada = models.CharField(verbose_name="Entrada", max_length=50, blank=True, null=True)
    obs_salida = models.CharField(verbose_name="Salida", max_length=50, blank=True, null=True)
    analisis = models.CharField(verbose_name="Análisis", max_length=50, blank=True, null=True)

    # Función que permite asignar el turno en base a la hora que ingresa y la hora que sale
    def asignar_turno(self):
        turnos_filtrados_a = Turnos.objects.filter(
            hora_inicial__lte=self.hora_registro_entrada, hora_final__lte=self.hora_registro_salida)
        turnos_filtrados_b = Turnos.objects.filter(
            hora_inicial__gte=self.hora_registro_entrada, hora_final__gte=self.hora_registro_salida)
        if turnos_filtrados_a.exists():
            self.turno = turnos_filtrados_a.first()
        elif turnos_filtrados_b.exists():
            self.turno = turnos_filtrados_b.first()
        else:
            self.turno = None

    # Función que permite guardar las observaciones y el análisis de los datos del biométrico
    def save(self, *args, **kwargs):
        self.justificacion = self.turno_programado.justificacion

        # Asigna fecha de registro el día que realizo registro en biometrico
        if (self.fecha_registro_entrada is not None):
            self.fecha_registro = self.fecha_registro_entrada
        else:
            self.fecha_registro = date.today()

        minutos_gracia = 10
        resultado_gracia = datetime.time(datetime.combine(datetime.today(
        ), self.turno_programado.turno.hora_inicial) + timedelta(minutes=minutos_gracia))

        hora_inicio_gracia = str(resultado_gracia)
        hora_inicio_turno_str = str(self.turno_programado.turno.hora_inicial)
        hora_fin_turno_str = str(self.turno_programado.turno.hora_final)
        turno_programado = self.turno_programado.turno.id_turno
        hora_entrada_formateada = str(self.hora_registro_entrada)
        hora_salida_formateada = str(self.hora_registro_salida)

        if (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and (hora_inicio_turno_str <= hora_entrada_formateada <= hora_inicio_gracia) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada >= hora_fin_turno_str):
            self.obs_marcacion = 'OK'
            self.obs_entrada = 'OK'
            self.obs_salida = 'OK'
            self.analisis = 'OK'
            self.asignar_turno()
        elif (self.fecha_registro_entrada is None and self.hora_registro_entrada is None) and (self.fecha_registro_salida is None and self.hora_registro_salida is None) and (turno_programado is not None and turno_programado == 'AU'):
            self.obs_marcacion = 'Sin marcación'
            self.obs_entrada = 'No marcó entrada'
            self.obs_salida = 'No marcó salida'
            self.analisis = 'Ausentismo'
            self.turno = Turnos.objects.get(id_turno='AU')
            self.fecha_registro = self.turno_programado.fecha_turno
        elif (self.fecha_registro_entrada is None and self.hora_registro_entrada is None) and (self.fecha_registro_salida is None and self.hora_registro_salida is None) and (turno_programado is not None and turno_programado == 'DL'):
            self.obs_marcacion = ''
            self.obs_entrada = ''
            self.obs_salida = ''
            self.analisis = 'Programado Día Libre'
            self.turno = Turnos.objects.get(id_turno='DL')
            self.fecha_registro = self.turno_programado.fecha_turno
        elif (self.fecha_registro_entrada is None and self.hora_registro_entrada is None) and (self.fecha_registro_salida is None and self.hora_registro_salida is None) and (turno_programado is not None and turno_programado == 'VC'):
            self.obs_marcacion = ''
            self.obs_entrada = ''
            self.obs_salida = ''
            self.analisis = 'Vacaciones'
            self.turno = Turnos.objects.get(id_turno='VC')
            self.fecha_registro = self.turno_programado.fecha_turno
        elif (self.fecha_registro_entrada is None and self.hora_registro_entrada is None) and (self.fecha_registro_salida is None and self.hora_registro_salida is None) and (turno_programado is not None and turno_programado == 'LI'):
            self.obs_marcacion = ''
            self.obs_entrada = ''
            self.obs_salida = ''
            self.analisis = 'Licencia/Incapacidad'
            self.turno = Turnos.objects.get(id_turno='LI')
            self.fecha_registro = self.turno_programado.fecha_turno
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and (((hora_inicio_turno_str >= hora_entrada_formateada) or (hora_inicio_turno_str <= hora_entrada_formateada)) and hora_entrada_formateada <= hora_inicio_gracia) and (self.fecha_registro_salida is None and self.hora_registro_salida is None):
            self.obs_marcacion = 'Solamente marcó entrada'
            self.obs_entrada = 'OK'
            self.obs_salida = 'No marcó salida'
            self.analisis = 'Revisar Marcaciones'
            self.turno = self.turno_programado.turno
        elif (self.fecha_registro_entrada is None and self.hora_registro_entrada is None) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada >= hora_fin_turno_str):
            self.obs_marcacion = 'Solamente marcó salida'
            self.obs_entrada = 'No marcó entrada'
            self.obs_salida = 'OK'
            self.analisis = 'Revisar Marcaciones'
            self.fecha_registro = self.fecha_registro_salida
            self.turno = self.turno_programado.turno
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and (hora_entrada_formateada > hora_inicio_gracia) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada >= hora_fin_turno_str):
            self.obs_marcacion = 'OK'
            self.obs_entrada = 'Llego Tarde'
            self.obs_salida = 'OK'
            self.analisis = 'Revisar Motivo de llegada tarde'
            self.asignar_turno()
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and (hora_entrada_formateada > hora_inicio_gracia) and (self.fecha_registro_salida is None and self.hora_registro_salida is None):
            self.obs_marcacion = 'Solamente marcó entrada'
            self.obs_entrada = 'Llego Tarde'
            self.obs_salida = 'No marcó salida'
            self.analisis = 'Revisar Marcaciones'
            self.turno = self.turno_programado.turno
        elif (self.fecha_registro_entrada is None and self.hora_registro_entrada is None) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada < hora_fin_turno_str):
            self.obs_marcacion = 'Solamente marcó salida'
            self.obs_entrada = 'No marcó entrada'
            self.obs_salida = 'Sale antes de hora'
            self.analisis = 'Revisar Marcaciones'
            self.fecha_registro = self.fecha_registro_salida
            self.turno = self.turno_programado.turno
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and (hora_entrada_formateada > hora_inicio_gracia) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada < hora_fin_turno_str):
            self.obs_marcacion = 'OK'
            self.obs_entrada = 'Llego Tarde'
            self.obs_salida = 'Sale antes de hora'
            self.analisis = 'Revisar Situación'
            self.asignar_turno()
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and ((hora_entrada_formateada <= hora_inicio_turno_str) or (hora_entrada_formateada <= hora_inicio_gracia)) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada >= hora_fin_turno_str):
            self.obs_marcacion = 'OK'
            self.obs_entrada = 'OK'
            self.obs_salida = 'OK'
            self.analisis = 'OK'
            self.asignar_turno()
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and (hora_entrada_formateada > hora_inicio_gracia) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada >= hora_fin_turno_str):
            self.obs_marcacion = 'OK'
            self.obs_entrada = 'Llego Tarde'
            self.obs_salida = 'OK'
            self.analisis = 'Revisar Motivo de llegada tarde'
            self.asignar_turno()
        elif (self.fecha_registro_entrada is not None and self.hora_registro_entrada is not None) and ((hora_entrada_formateada <= hora_inicio_turno_str) or (hora_entrada_formateada <= hora_inicio_gracia)) and (self.fecha_registro_salida is not None and self.hora_registro_salida is not None) and (hora_salida_formateada < hora_fin_turno_str):
            self.obs_marcacion = 'OK'
            self.obs_entrada = 'OK'
            self.obs_salida = 'Sale antes de hora'
            self.analisis = 'Revisar Marcaciones'
            self.asignar_turno()
        else:
            self.obs_marcacion = ''
            self.obs_entrada = ''
            self.obs_salida = ''
            self.analisis = ''
            self.turno = None
            self.justificacion = None
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return 'Registro {}'.format(self.id_registro)
