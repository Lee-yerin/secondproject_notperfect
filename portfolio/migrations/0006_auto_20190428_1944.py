# Generated by Django 2.1.7 on 2019-04-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20190428_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='text',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
