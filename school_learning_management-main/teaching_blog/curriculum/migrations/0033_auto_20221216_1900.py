# Generated by Django 3.2 on 2022-12-16 18:00

import curriculum.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0032_auto_20221216_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['position']},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='added',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Video'),
        ),
    ]