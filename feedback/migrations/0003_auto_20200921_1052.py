# Generated by Django 3.1.1 on 2020-09-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['datetime'], 'verbose_name_plural': 'feedback'},
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
