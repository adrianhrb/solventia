# Generated by Django 5.0 on 2023-12-05 16:16

import queues.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0004_alter_queue_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='color',
            field=models.CharField(blank=True, default=queues.utils.get_random_rgb, max_length=13),
        ),
    ]