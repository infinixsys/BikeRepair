# Generated by Django 4.1.7 on 2023-04-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_mechanic_aadhar_mechanic_qualifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='aadhar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
