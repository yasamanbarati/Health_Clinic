# Generated by Django 3.2.8 on 2022-03-29 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_alter_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
