# Generated by Django 4.0.5 on 2022-06-17 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_remove_period_classroom_period_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='attendance.subjectteacher'),
        ),
    ]