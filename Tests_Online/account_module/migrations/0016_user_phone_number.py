# Generated by Django 3.2.8 on 2022-06-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0015_auto_20220610_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=11, null=True, verbose_name=''),
        ),
    ]