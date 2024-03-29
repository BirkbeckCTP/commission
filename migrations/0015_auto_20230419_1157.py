# Generated by Django 3.2.16 on 2023-04-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0014_commissionedarticle_additional_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionedarticle',
            name='submission_deadline',
            field=models.DateField(help_text='The deadline by which the author must submit the article.', null=True),
        ),
        migrations.AlterField(
            model_name='commissionedarticle',
            name='author_decision',
            field=models.CharField(blank=True, choices=[('accepted', 'Accepted'), ('declined', 'Declined')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='commissionedarticle',
            name='deadline',
            field=models.DateField(blank=True, help_text='The deadline by which the author must accept or decline the commission reuqest.', null=True),
        ),
    ]
