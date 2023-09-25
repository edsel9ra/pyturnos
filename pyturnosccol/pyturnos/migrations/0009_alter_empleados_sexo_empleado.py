# Generated by Django 4.2.4 on 2023-09-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyturnos', '0008_alter_turnos_tipo_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='sexo_empleado',
            field=models.CharField(choices=[('M', 'Masculino'), ('NB', 'No Binario'), ('F', 'Femenino')], max_length=2, verbose_name='Sexo/Genero'),
        ),
    ]