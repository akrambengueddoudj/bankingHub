# Generated by Django 5.0.3 on 2024-03-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='barcode_image',
            field=models.ImageField(blank=True, null=True, upload_to='barcodes/'),
        ),
    ]
