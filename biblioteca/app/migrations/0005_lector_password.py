# Generated by Django 4.1.1 on 2022-10-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='password',
            field=models.CharField(default='asd', max_length=255),
            preserve_default=False,
        ),
    ]
