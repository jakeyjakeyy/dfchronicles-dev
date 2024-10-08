# Generated by Django 4.2.4 on 2023-10-06 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0011_artifact_structure_local_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entities',
            name='hf_id',
        ),
        migrations.AddField(
            model_name='entities',
            name='profession',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='entities',
            name='weapon',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='entities',
            name='worship_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worship_hf_entities', to='chronicle_compiler.historicalfigures'),
        ),
    ]
