# Generated by Django 5.0.3 on 2024-03-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('id_number', models.CharField(max_length=100)),
                ('berry_weight', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
