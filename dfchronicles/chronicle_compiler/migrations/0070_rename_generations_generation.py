# Generated by Django 4.2.4 on 2023-11-15 08:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chronicle_compiler', '0069_generations_generation_rating_favorite_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Generations',
            new_name='Generation',
        ),
    ]
