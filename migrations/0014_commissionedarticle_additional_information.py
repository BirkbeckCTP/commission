# Generated by Django 3.2.16 on 2023-04-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0013_auto_20230404_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionedarticle',
            name='additional_information',
            field=models.TextField(blank=True, help_text='Add any information you want to provide to the author on the accept/decline page.', null=True),
        ),
    ]
