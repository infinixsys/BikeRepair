# Generated by Django 4.1.7 on 2023-04-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_alter_mechanic_aadhar'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='service_types',
            field=models.CharField(blank=True, choices=[('onetime', 'onetime'), ('yearly', 'yearly'), ('monthly', 'monthly')], max_length=200, null=True),
        ),
    ]
