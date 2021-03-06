# Generated by Django 3.1.7 on 2021-06-19 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (0, 'Female')], null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, default='')),
                ('avatar', models.ImageField(blank=True, default='avatar/no_avatar.png', upload_to=user_profile.models.upload_to)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
