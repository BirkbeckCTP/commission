# Generated by Django 3.2.16 on 2023-03-30 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commission', '0002_commissionedarticle_message_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commissionedarticle',
            name='commissioning_editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
