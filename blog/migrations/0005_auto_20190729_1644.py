# Generated by Django 2.2 on 2019-07-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_t_event_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_event',
            name='timeline',
            field=models.CharField(choices=[('inverted', 'inverted'), ('standard', 'standard')], default='', max_length=10),
        ),
    ]
