# Generated by Django 3.2.4 on 2021-06-05 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='locations.neighborhood'),
            preserve_default=False,
        ),
    ]
