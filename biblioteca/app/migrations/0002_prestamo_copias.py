# Generated by Django 4.1.1 on 2022-10-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='copias',
            field=models.ManyToManyField(to='app.copia'),
        ),
    ]
