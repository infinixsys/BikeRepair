# Generated by Django 4.1.7 on 2023-05-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0013_delete_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='status',
            field=models.CharField(blank=True, choices=[('approved', 'approved'), ('disapproved', 'disapproved')], default='disapproved', max_length=200, null=True),
        ),
    ]