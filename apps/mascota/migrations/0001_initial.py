# Generated by Django 2.0.1 on 2018-01-15 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_aproximada', models.DateField()),
            ],
        ),
    ]
