# Generated by Django 5.0.3 on 2024-03-16 10:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.CharField(choices=[('f', 'Free'), ('p', 'Payed'), ('b', 'Bank')], default='f', max_length=1)),
                ('payement_date_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayementRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/recipes/')),
                ('status', models.CharField(choices=[('a', 'Accepted'), ('r', 'Rejected'), ('n', 'New')], default='n', max_length=1)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payements', to='accounts.userprofile')),
            ],
        ),
    ]
