# Generated by Django 4.2.7 on 2023-12-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav',
            name='des',
            field=models.CharField(max_length=500),
        ),
    ]
