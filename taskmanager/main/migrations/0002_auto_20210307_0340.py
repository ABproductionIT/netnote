# Generated by Django 3.1.6 on 2021-03-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Head'),
        ),
    ]
