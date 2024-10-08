# Generated by Django 4.2.4 on 2023-10-14 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle_compiler', '0054_remove_circumstance_hist_event_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='danceforms',
            name='chronicle_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='danceforms',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='danceforms',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='danceforms',
            name='world',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_dance_forms', to='chronicle_compiler.world'),
        ),
        migrations.AddField(
            model_name='musicalforms',
            name='chronicle_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musicalforms',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='musicalforms',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='musicalforms',
            name='world',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_musical_forms', to='chronicle_compiler.world'),
        ),
        migrations.AddField(
            model_name='poeticforms',
            name='chronicle_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poeticforms',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='poeticforms',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='poeticforms',
            name='world',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='world_poetic_forms', to='chronicle_compiler.world'),
        ),
    ]
