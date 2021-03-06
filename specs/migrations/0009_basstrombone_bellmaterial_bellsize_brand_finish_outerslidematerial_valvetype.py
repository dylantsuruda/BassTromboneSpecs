# Generated by Django 3.1.1 on 2020-09-20 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0008_auto_20200920_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='BellMaterial',
            fields=[
                ('bell_material', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BellSize',
            fields=[
                ('bell_size', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Bell size (inches)')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Finish',
            fields=[
                ('finish', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OuterSlideMaterial',
            fields=[
                ('outer_slide_material', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ValveType',
            fields=[
                ('valve_type', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BassTrombone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('number_of_valves', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double')], max_length=6)),
                ('valve_configuration', models.CharField(choices=[('Not applicable', 'Not applicable'), ('Dependent', 'Dependent'), ('Independent', 'Independent')], max_length=14)),
                ('wrap', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=6)),
                ('dual_bore', models.CharField(choices=[('Dual bore', 'Dual bore'), ('Not dual bore', 'Not dual bore')], max_length=13)),
                ('bell_material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.bellmaterial')),
                ('bell_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.bellsize')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.brand')),
                ('finish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.finish')),
                ('outer_slide_material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.outerslidematerial')),
                ('valve_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specs.valvetype')),
            ],
        ),
    ]
