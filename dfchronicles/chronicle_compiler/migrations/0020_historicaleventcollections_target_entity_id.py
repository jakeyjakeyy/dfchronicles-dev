# Generated by Django 4.2.4 on 2023-10-07 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0019_remove_historicaleventcollections_eventcol_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaleventcollections',
            name='target_entity_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='target_historical_event_collections', to='chronicle_compiler.entities'),
        ),
    ]
