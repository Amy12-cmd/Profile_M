# Generated by Django 4.2.6 on 2023-11-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynxe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Amol_Sutar1.jpg', null=True, upload_to='images/'),
        ),
    ]
