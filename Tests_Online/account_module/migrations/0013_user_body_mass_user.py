# Generated by Django 3.2.8 on 2022-04-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0012_remove_user_body_mass_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='body_mass_user',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='وضعیت توده بندی کاربر'),
        ),
    ]