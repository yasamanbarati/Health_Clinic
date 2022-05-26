from django.db import models

# Create your models here.


class Responsibility(models.Model):
    title = models.CharField(max_length=300, verbose_name=' عنوان مسیولیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مسیولیت'
        verbose_name_plural = 'لیست مسیولیت'


class MembersInfo(models.Model):
    responsibility = models.ForeignKey(Responsibility, on_delete=models.CASCADE, verbose_name='مسیولیت')
    name = models.CharField(max_length=300, verbose_name='نام')
    avatar = models.ImageField(upload_to='images/team_info', verbose_name='تصویر')
    url_linkedin = models.URLField(verbose_name='لینک linkedin')
    url_whatsapp = models.URLField(verbose_name='لینک whatsapp')
    url_telegram = models.URLField(verbose_name='لینک telegram')
    url_email = models.URLField(verbose_name='لینک email')
    short_descriptions = models.TextField(verbose_name='توضیح کوتاه')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اعضا'
        verbose_name_plural = 'اعضای گروه'

