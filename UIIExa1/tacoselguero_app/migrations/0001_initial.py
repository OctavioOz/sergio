# Generated by Django 5.1 on 2024-10-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.PositiveSmallIntegerField()),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('orden', models.CharField(max_length=100)),
                ('pago', models.CharField(max_length=100)),
                ('cantidad', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
