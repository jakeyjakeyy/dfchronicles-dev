# Generated by Django 4.2.4 on 2023-10-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0016_remove_historicaleventcollections_attacking_squad_entity_pop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitypopulations',
            name='population',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='entitypopulations',
            name='race',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
