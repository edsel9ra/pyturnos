# Generated by Django 4.2.4 on 2023-09-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyturnos', '0007_alter_empleados_sexo_empleado_alter_turnos_id_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='tipo_turno',
            field=models.CharField(blank=True, choices=[('AST', 'Asistencial'), ('ADM', 'Administrativo'), ('24H', 'Día Completo')], max_length=3, null=True, verbose_name='Tipo Turno'),
        ),
    ]
