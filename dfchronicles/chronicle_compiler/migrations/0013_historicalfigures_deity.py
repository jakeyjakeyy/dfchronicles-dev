# Generated by Django 4.2.4 on 2023-10-06 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0012_remove_entities_hf_id_entities_profession_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalfigures',
            name='deity',
            field=models.BooleanField(default=False),
        ),
    ]
