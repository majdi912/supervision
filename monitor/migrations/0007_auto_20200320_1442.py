# Generated by Django 3.0.2 on 2020-03-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20200319_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panne',
            name='date_panne',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='panne',
            name='date_reparation',
            field=models.CharField(max_length=20),
        ),
    ]
