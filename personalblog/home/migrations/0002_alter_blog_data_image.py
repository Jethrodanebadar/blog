# Generated by Django 5.0.6 on 2024-05-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_data',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]