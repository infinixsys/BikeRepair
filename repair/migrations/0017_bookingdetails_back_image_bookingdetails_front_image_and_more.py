# Generated by Django 4.1.7 on 2023-05-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0016_alter_mechanic_aadhar'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='front_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='left_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='right_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
