# Generated by Django 3.2.4 on 2021-06-05 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_neighborhood'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Neighborhood',
        ),
    ]