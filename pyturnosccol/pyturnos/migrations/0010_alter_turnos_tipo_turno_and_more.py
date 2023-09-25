# Generated by Django 4.2.4 on 2023-09-07 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyturnos', '0009_alter_empleados_sexo_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='tipo_turno',
            field=models.CharField(blank=True, choices=[('ADM', 'Administrativo'), ('AST', 'Asistencial'), ('24H', 'Día Completo')], max_length=3, null=True, verbose_name='Tipo Turno'),
        ),
        migrations.AlterField(
            model_name='turnosprogramados',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos_programados', to='pyturnos.empleados', verbose_name='Empleado'),
        ),
    ]