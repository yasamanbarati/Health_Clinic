# Generated by Django 3.2.8 on 2022-06-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BMI_module', '0011_diseasecategorygroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasegroupmodels',
            name='caregory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BMI_module.diseasecategorygroup', verbose_name='بیماری اصلی'),
        ),
    ]
