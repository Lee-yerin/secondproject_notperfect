# Generated by Django 2.1.7 on 2019-04-30 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190428_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='grade',
            field=models.IntegerField(max_length=100),
        ),
    ]
