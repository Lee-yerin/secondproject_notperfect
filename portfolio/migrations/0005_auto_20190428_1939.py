# Generated by Django 2.1.7 on 2019-04-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20190428_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='text',
            field=models.TextField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='grade',
            field=models.TextField(max_length=100),
        ),
    ]