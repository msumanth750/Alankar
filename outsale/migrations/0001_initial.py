# Generated by Django 3.1.13 on 2022-04-20 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outsale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('name', models.CharField(default='Customer', max_length=30)),
                ('udate', models.DateField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
        ),
    ]