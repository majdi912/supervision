# Generated by Django 3.0.2 on 2020-03-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_auto_20200320_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='nbre_port',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='num_port',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='switch',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='panne',
            name='date_panne',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='panne',
            name='date_reparation',
            field=models.CharField(max_length=50),
        ),
    ]
