# Generated by Django 4.1.1 on 2022-09-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_new_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
