# Generated by Django 3.1.7 on 2021-08-28 10:57

import actions.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedislike',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=actions.models.like_limit, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]