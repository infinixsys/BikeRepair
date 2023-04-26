# Generated by Django 4.1.7 on 2023-04-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('priority', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddOfferBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('priority', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
