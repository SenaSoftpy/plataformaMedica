# Generated by Django 3.1.2 on 2020-10-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorizaciones',
            fields=[
                ('id_autorizacion', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_autorizacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id_diagnostico', models.IntegerField(primary_key=True, serialize=False)),
                ('sintomas', models.CharField(max_length=500)),
                ('resultado_diagnos', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id_historia', models.IntegerField(primary_key=True, serialize=False)),
                ('date_aperturaHist', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Interaccion',
            fields=[
                ('id_interaccion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_mensaje', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_medico', models.IntegerField(primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('especialidad', models.CharField(max_length=100)),
                ('rol', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('idAutorización', models.IntegerField()),
                ('nombre_paciente', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.IntegerField(primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('dias_incapacidad', models.CharField(max_length=100)),
                ('resultados_examenes', models.TextField()),
                ('rol', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_cambioMedico',
            fields=[
                ('id_solicMed', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.TextField()),
                ('medico_actual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_grupoFam',
            fields=[
                ('id_solicFam', models.AutoField(primary_key=True, serialize=False)),
                ('idGrupoFam', models.IntegerField()),
                ('integrantes', models.TextField()),
            ],
        ),
    ]
