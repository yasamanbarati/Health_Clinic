# Generated by Django 3.2.8 on 2022-06-09 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BMI_module', '0019_remove_comment_name'),
        ('account_module', '0013_user_body_mass_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sickness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BMI_module.diseasegroupmodels', verbose_name='بیماری کاربر'),
        ),
    ]
