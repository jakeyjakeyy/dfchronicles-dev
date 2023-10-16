# Generated by Django 4.2.4 on 2023-10-16 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0058_alter_danceforms_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='writtencontents',
            name='reference',
        ),
        migrations.CreateModel(
            name='MountainPeak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chronicle_id', models.IntegerField()),
                ('name', models.CharField(null=True)),
                ('coords', models.CharField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('volcano', models.BooleanField(default=False, null=True)),
                ('world', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_mountain_peak', to='chronicle_compiler.world')),
            ],
        ),
        migrations.CreateModel(
            name='Landmass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chronicle_id', models.IntegerField()),
                ('name', models.CharField(null=True)),
                ('coord1', models.CharField(null=True)),
                ('coord2', models.CharField(null=True)),
                ('world', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_landmass', to='chronicle_compiler.world')),
            ],
        ),
    ]
