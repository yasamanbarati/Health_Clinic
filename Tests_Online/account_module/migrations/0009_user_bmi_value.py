# Generated by Django 3.2.8 on 2022-04-24 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0008_alter_user_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='BMI_value',
            field=models.IntegerField(default=0, verbose_name='مقدار BMI'),
        ),
    ]
