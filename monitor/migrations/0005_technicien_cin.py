# Generated by Django 3.0.2 on 2020-03-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20200318_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicien',
            name='cin',
            field=models.BigIntegerField(null=True),
        ),
    ]
