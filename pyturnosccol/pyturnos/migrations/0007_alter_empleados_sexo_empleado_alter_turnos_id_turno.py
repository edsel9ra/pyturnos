# Generated by Django 4.2.4 on 2023-09-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyturnos', '0006_alter_empleados_sexo_empleado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='sexo_empleado',
            field=models.CharField(choices=[('NB', 'No Binario'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=2, verbose_name='Sexo/Genero'),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='id_turno',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]