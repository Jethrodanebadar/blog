# Generated by Django 5.0.6 on 2024-05-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_blog_data_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_data',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
