# Generated by Django 2.0.4 on 2018-04-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180424_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='value',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]
