# Generated by Django 3.0.5 on 2020-09-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='damage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='environment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='injury',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='vehicle',
            field=models.BooleanField(default=False),
        ),
    ]
