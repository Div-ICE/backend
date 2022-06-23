# Generated by Django 3.2.13 on 2022-06-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True, verbose_name='Организация'),
        ),
    ]