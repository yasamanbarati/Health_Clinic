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
    caregory = models.ForeignKey('DiseaseGroupModels', on_delete=models.CASCADE, verbose_name='بیماری والد', null=True
                                 , blank=True)
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


class VideoResultModels(models.Model):
    Body_mass = models.ForeignKey(BodyMassModels, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='مناسب برای توده بندی ')
    video_result = models.FileField(upload_to='video/result', verbose_name='فایل ویدیو')
    name = models.CharField(max_length=300, verbose_name='نام ویدیو')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'لیست ویدیو'


class FoodModels(models.Model):
    Body_mass = models.ForeignKey(BodyMassModels, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='مناسب برای توده بندی ')
    image_food = models.ImageField(upload_to='images/foods', verbose_name='تصویر', null=True, blank=True)
    pdf_food = models.FileField(upload_to='pdf/food', verbose_name='فایل pdf', )
    # video_result = models.FileField(upload_to='video/result', verbose_name='فایل ویدیو', )
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


class Comment(models.Model):
    # name = models.CharField(max_length=200,verbose_name='نام کاربر', null=True, blank=True)
    text_comment = models.TextField(verbose_name='متن پیام')
    created_comment = models.DateTimeField(verbose_name='تاریخ ایجاد شده', auto_now_add=True)
    active_comment = models.BooleanField(default=False, verbose_name='فعال/ غیر فعال')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f"{self.created_comment} , {self.active_comment}"

# class Events(models.Model):
#     image_food = models.ImageField(upload_to='images/foods', verbose_name='تصویر', null=True, blank=True)
#     name = models.CharField(max_length=300, verbose_name='نام غذا')
