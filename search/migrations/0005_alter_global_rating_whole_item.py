# Generated by Django 4.1.7 on 2023-03-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_global_rating_whole_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global_rating',
            name='whole_item',
            field=models.JSONField(default=dict),
        ),
    ]
