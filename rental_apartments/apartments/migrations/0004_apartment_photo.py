# Generated by Django 4.1.3 on 2022-12-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_alter_guest_user_alter_reservation_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo'),
        ),
    ]
