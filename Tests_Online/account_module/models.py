from django.contrib.auth.models import AbstractUser
from django.db import models
from BMI_module.models import BodyMassModels
from BMI_module.models import DiseaseGroupModels


class User(AbstractUser):
    users_name = models.CharField(max_length=300, verbose_name='ایدی', null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='تلفن همراه', max_length=11, blank=True, null=True)
    # avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=True, blank=True)
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال شازی ایمیل')
    about_text = models.TextField(null=True, blank=True, verbose_name='در باره شما')
    height = models.PositiveIntegerField(null=True, blank=True, verbose_name='قد')
    weight = models.PositiveIntegerField(null=True, blank=True, verbose_name='وزن')
    BMI_value = models.IntegerField(default=0, verbose_name='مقدار BMI')
    body_mass_user = models.CharField(max_length=300, verbose_name='وضعیت توده بندی کاربر', null=True, blank=True)
    sickness = models.ManyToManyField(DiseaseGroupModels, blank=True, null=True, verbose_name='بیماری کاربر')

    # body_mass_user = models.CharField(max_length='300', verbose_name='وضعیت توده بندی کاربر', null=True, blank=True)
    # body_mass_user = models.ForeignKey(BodyMassModels, on_delete=models.CASCADE, verbose_name='وضعیت توده بندی کاربر',
    #                               null=True, blank=True )
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email

