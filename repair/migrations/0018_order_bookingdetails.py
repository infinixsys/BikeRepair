# Generated by Django 4.1.7 on 2023-05-15 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0017_bookingdetails_back_image_bookingdetails_front_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bookingdetails',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.bookingdetails'),
        ),
    ]
