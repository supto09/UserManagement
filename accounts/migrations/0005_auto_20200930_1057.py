# Generated by Django 3.1.1 on 2020-09-30 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200928_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birthDate',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
