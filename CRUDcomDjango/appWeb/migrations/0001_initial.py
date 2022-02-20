# Generated by Django 4.0.2 on 2022-02-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Req_nome', models.CharField(max_length=30)),
                ('Mat_nro', models.IntegerField()),
                ('Curso_nome', models.CharField(max_length=30)),
                ('Sala_nro', models.IntegerField()),
                ('Data', models.DateField()),
                ('Horario', models.TimeField()),
            ],
        ),
    ]