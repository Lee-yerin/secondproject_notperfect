# Generated by Django 2.1.7 on 2019-04-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190428_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='hometown',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='major',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]