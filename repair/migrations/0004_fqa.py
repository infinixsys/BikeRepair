# Generated by Django 4.1.7 on 2023-04-19 01:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_support_contact_support_name_support_txt'),
    ]

    operations = [
        migrations.CreateModel(
            name='FQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('answer', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
            ],
        ),
    ]