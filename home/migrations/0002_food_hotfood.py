# Generated by Django 5.0.6 on 2024-05-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='hotFood',
            field=models.BooleanField(default=False),
        ),
    ]