# Generated by Django 5.0 on 2023-12-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0003_alter_queue_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='color',
            field=models.CharField(blank=True, default='75,92,106', max_length=13),
        ),
    ]
