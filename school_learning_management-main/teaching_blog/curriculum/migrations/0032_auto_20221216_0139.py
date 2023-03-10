# Generated by Django 3.2 on 2022-12-16 00:39

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0031_auto_20221215_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['position', 'added']},
        ),
        migrations.AddField(
            model_name='lesson',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
