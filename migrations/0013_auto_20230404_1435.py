# Generated by Django 3.2.16 on 2023-04-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0012_auto_20230403_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionedarticle',
            name='reminder_after_sent',
            field=models.DateTimeField(blank=True, help_text='The date and time the after deadline reminder is sent.', null=True),
        ),
        migrations.AddField(
            model_name='commissionedarticle',
            name='reminder_before_sent',
            field=models.DateTimeField(blank=True, help_text='The date and time the before deadline reminder is sent.', null=True),
        ),
    ]
