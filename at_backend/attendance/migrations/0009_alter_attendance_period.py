# Generated by Django 4.0.5 on 2022-06-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_delete_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='period',
            field=models.IntegerField(default=1),
        ),
    ]
