# Generated by Django 4.2.4 on 2023-10-10 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0040_historicalevents_first_historicalevents_knowledge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteproperty',
            name='structure_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='structure_site_property', to='chronicle_compiler.structures'),
        ),
        migrations.AlterField(
            model_name='siteproperty',
            name='type',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
