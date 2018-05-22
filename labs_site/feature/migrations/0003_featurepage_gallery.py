# Generated by Django 2.0.5 on 2018-05-20 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('feature', '0002_auto_20180520_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurepage',
            name='gallery',
            field=models.ForeignKey(blank=True, help_text='Select the image collection for this gallery.', limit_choices_to=models.Q(_negated=True, name__in=['Root']), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Collection'),
        ),
    ]
