# Generated by Django 4.1.7 on 2023-05-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0010_service_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]