# Generated by Django 4.1.7 on 2023-04-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='aadhar',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='qualifications',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='upload_aadhar',
            field=models.FileField(blank=True, null=True, upload_to='aadhar/'),
        ),
    ]
