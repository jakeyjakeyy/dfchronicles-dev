# Generated by Django 4.2.4 on 2023-10-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0033_entitypositionlink_civ_id_intrigueactor_civ_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationshipprofilevisual',
            name='rep_information_source',
            field=models.IntegerField(null=True),
        ),
    ]
