# Generated by Django 2.0.5 on 2018-05-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurepage',
            name='description',
            field=models.TextField(help_text='Describe the feature'),
        ),
    ]
