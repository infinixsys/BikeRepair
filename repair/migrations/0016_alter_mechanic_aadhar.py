# Generated by Django 4.1.7 on 2023-05-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0015_alter_mechanic_aadhar_alter_mechanic_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='aadhar',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
    ]