# Generated by Django 3.1.1 on 2020-09-20 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0003_delete_customizablebasstrombone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizableBassTrombone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trombone', models.CharField(max_length=100)),
            ],
        ),
    ]
