# Generated by Django 4.1.7 on 2023-03-31 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0006_planname_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='planname',
            name='services',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
