# Generated by Django 3.0.7 on 2020-09-12 15:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200909_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='article/main_images', verbose_name='Əsas şəkil'),
        ),
    ]
