# Generated by Django 4.2.4 on 2023-10-10 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0041_siteproperty_structure_id_alter_siteproperty_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalevents',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='historicalevents',
            name='position_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='position_historical_events', to='chronicle_compiler.entityposition'),
        ),
        migrations.AddField(
            model_name='structures',
            name='subtype',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
