# Generated by Django 4.1.7 on 2023-05-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0009_service_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
