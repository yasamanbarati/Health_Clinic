# Generated by Django 3.2.8 on 2022-04-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMI_module', '0009_auto_20220404_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmimodels',
            name='height',
            field=models.FloatField(verbose_name='قد'),
        ),
        migrations.AlterField(
            model_name='bmimodels',
            name='weight',
            field=models.FloatField(verbose_name='وزن'),
        ),
    ]
