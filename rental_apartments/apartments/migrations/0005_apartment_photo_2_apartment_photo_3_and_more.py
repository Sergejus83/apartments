# Generated by Django 4.1.3 on 2022-12-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_apartment_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo'),
        ),
    ]