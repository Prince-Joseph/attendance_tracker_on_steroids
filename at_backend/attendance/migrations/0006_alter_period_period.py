# Generated by Django 4.0.5 on 2022-06-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_period_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='period',
            field=models.IntegerField(default=1),
        ),
    ]
