# Generated by Django 4.1.2 on 2022-10-10 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='price')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='api.section')),
            ],
        ),
    ]