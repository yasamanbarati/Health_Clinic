# Generated by Django 3.2.8 on 2022-06-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0014_auto_20220608_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='uploads/default-profile-pic.jpg', null=True, upload_to='images/profile', verbose_name='تصویر آواتار'),
        ),
    ]
