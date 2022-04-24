# Generated by Django 3.1.13 on 2022-04-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('stock', '0004_auto_20220410_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receits',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand'),
        ),
    ]
