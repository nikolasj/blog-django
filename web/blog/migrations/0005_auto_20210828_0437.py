# Generated by Django 3.1.7 on 2021-08-28 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210718_0740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-id',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
