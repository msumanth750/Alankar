# Generated by Django 3.1.13 on 2022-04-10 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='obal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]