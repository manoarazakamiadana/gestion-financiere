# Generated by Django 4.2.13 on 2024-07-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateinterval',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='dateinterval',
            name='start',
            field=models.DateField(null=True),
        ),
    ]