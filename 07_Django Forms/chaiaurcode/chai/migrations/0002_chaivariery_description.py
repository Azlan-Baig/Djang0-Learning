# Generated by Django 5.0.6 on 2024-06-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariery',
            name='description',
            field=models.TextField(default=''),
        ),
    ]