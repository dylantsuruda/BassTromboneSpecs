# Generated by Django 3.1.1 on 2020-09-20 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0005_auto_20200920_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='BellMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bell_material', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BellSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bell_size', models.CharField(max_length=5, verbose_name='Bell size (inches)')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Finish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OuterSlideMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer_slide_material', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ValveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valve_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='basstrombone',
            name='bell_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.bellmaterial'),
        ),
        migrations.AlterField(
            model_name='basstrombone',
            name='bell_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.bellsize'),
        ),
        migrations.AlterField(
            model_name='basstrombone',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.brand'),
        ),
        migrations.AlterField(
            model_name='basstrombone',
            name='finish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.finish'),
        ),
        migrations.AlterField(
            model_name='basstrombone',
            name='outer_slide_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.outerslidematerial'),
        ),
        migrations.AlterField(
            model_name='basstrombone',
            name='valve_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.valvetype'),
        ),
    ]
