# Generated by Django 4.1.2 on 2022-10-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_modifier_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifier',
            name='items',
            field=models.ManyToManyField(to='api.item'),
        ),
    ]