# Generated by Django 3.0.11 on 2021-02-01 14:48

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210201_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='article/main_images', verbose_name='Əsas şəkil *'),
        ),
    ]
