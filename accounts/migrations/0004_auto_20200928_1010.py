# Generated by Django 3.1.1 on 2020-09-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200928_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobby',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
