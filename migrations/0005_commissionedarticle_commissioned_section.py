# Generated by Django 3.2.16 on 2023-03-30 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0004_auto_20230330_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionedarticle',
            name='commissioned_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='submission.section'),
        ),
    ]
