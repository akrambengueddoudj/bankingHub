# Generated by Django 5.0.3 on 2024-03-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
