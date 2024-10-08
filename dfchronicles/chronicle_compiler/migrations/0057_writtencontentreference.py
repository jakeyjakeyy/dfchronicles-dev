# Generated by Django 4.2.4 on 2023-10-16 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0056_regions_coords_regions_force_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WrittenContentReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dance_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dance_form_written_content_reference', to='chronicle_compiler.danceforms')),
                ('musical_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='musical_form_written_content_reference', to='chronicle_compiler.musicalforms')),
                ('poetic_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poetic_form_written_content_reference', to='chronicle_compiler.poeticforms')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_written_content_reference', to='chronicle_compiler.sites')),
                ('world', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_written_content_reference', to='chronicle_compiler.world')),
                ('written_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_content_written_content_reference', to='chronicle_compiler.writtencontents')),
            ],
        ),
    ]
