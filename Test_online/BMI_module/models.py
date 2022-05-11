from django.db import models

# Create your models here.
from django.urls import reverse


class BMIModels(models.Model):
    Gender_choices = (
        ('آقا', 'آقا'),
        ('خانم', 'خانم')
    )
    weight = models.FloatField(verbose_name='وزن')
    height = models.FloatField(verbose_name='قد')
    age = models.IntegerField(verbose_name='سن')
    gender = models.CharField(max_length=20, choices=Gender_choices, default='آقا')

    class Meta:
        verbose_name = 'BMI'
        verbose_name_plural = 'لیست BMI'

    # def get_BMI(self):
    #     res = pow(self.height, 2)/self.weight
    #     return res

    def __str__(self):
        return str(self.weight)


class DiseaseGroupModels(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام بیماری')
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, verbose_name='نام در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بیماری'
        verbose_name_plural = 'لیست بیماری ها'

    def get_absolute_url(self):
        return reverse('disease_group', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class BodyMassModels(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام توده بدنی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توده بدنی'
        verbose_name_plural = 'لیست توده بدنی'


class FoodModels(models.Model):
    Body_mass = models.ForeignKey(BodyMassModels, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='مناسب برای توده بندی ')
    name = models.CharField(max_length=300, verbose_name='نام غذا')
    group = models.ManyToManyField(DiseaseGroupModels, verbose_name='گروه بیماری')
    short_description = models.TextField(verbose_name='توضیخات اولیه', null=True, blank=True)
    raw_material = models.TextField(verbose_name='مواد اولیه')
    description = models.TextField(verbose_name='طرز تهیه')
    informations_food = models.TextField(verbose_name='اطلاعات علمی در باره غذا', null=True, blank=True)
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, verbose_name='نام در url')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'لیست غذا'

    def get_absolute_url(self):
        return reverse('disease_group', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
