import os
from django.http import HttpResponse, Http404
from Test_online import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from account_module.models import User
from . import forms
from . import models
import json


# محاسبه توده بدنی افراد بالای 20 سال
def calculate_Body_mass(bmi):
    if bmi < 18.5:
        return 'کمبود وزن'
    elif 18.5 <= bmi <= 24.9:
        return 'نرمال'
    elif 25 <= bmi <= 29.9:
        return 'اضافه وزن'
    elif 30 <= bmi <= 34.9:
        return 'چاق'
    elif bmi >= 35:
        return 'خیلی چاق'


# محاسبه توده بدنی خانم زیر 20 سال
def calculate_Body_Girl_mass(bmi, age):
    if age == 2:
        if bmi < 14.5:
            return 'کمبود وزن'
        elif 14.5 <= bmi <= 18:
            return 'نرمال'
        elif 18 < bmi <= 19:
            return 'چاق'
    elif age == 3:
        if bmi < 14:
            return 'کمبود وزن'
        elif 14 <= bmi <= 17.2:
            return 'نرمال'
        elif 17.2 < bmi <= 18:
            return 'اضافه وزن'
        elif bmi > 18:
            return 'چاق'
    elif age == 4:
        if bmi < 13.6:
            return 'کمبود وزن'
        elif 13.7 <= bmi <= 16.9:
            return 'نرمال'
        elif 17 < bmi <= 18:
            return 'اضافه وزن'
        elif bmi > 18:
            return 'چاق'
    elif age == 5:
        if bmi < 13.2:
            return 'کمبود وزن'
        elif 13.3 <= bmi <= 17.1:
            return 'نرمال'
        elif 17.2 < bmi <= 18.5:
            return 'اضافه وزن'
        elif bmi > 18.5:
            return 'چاق'
    elif age == 6:
        if bmi < 13.4:
            return 'کمبود وزن'
        elif 13.5 <= bmi <= 17.2:
            return 'نرمال'
        elif 17.2 < bmi <= 19:
            return 'اضافه وزن'
        elif bmi > 19:
            return 'چاق'
    elif age == 7:
        if bmi < 13.5:
            return 'کمبود وزن'
        elif 13.6 <= bmi <= 18:
            return 'نرمال'
        elif 18 < bmi <= 20:
            return 'اضافه وزن'
        elif bmi > 20:
            return 'چاق'
    elif age == 8:
        if bmi < 13.6:
            return 'کمبود وزن'
        elif 13.7 <= bmi <= 18.4:
            return 'نرمال'
        elif 18.3 < bmi <= 21:
            return 'اضافه وزن'
        elif bmi > 21:
            return 'چاق'
    elif age == 9:
        if bmi < 14:
            return 'کمبود وزن'
        elif 14 <= bmi <= 17.9:
            return 'نرمال'
        elif 18 < bmi <= 22:
            return 'اضافه وزن'
        elif bmi > 22:
            return 'چاق'
    elif age == 10:
        if bmi < 14.2:
            return 'کمبود وزن'
        elif 14.3 <= bmi <= 18.6:
            return 'نرمال'
        elif 18.6 < bmi <= 23:
            return 'اضافه وزن'
        elif bmi > 23:
            return 'چاق'
    elif age == 11:
        if bmi < 14.6:
            return 'کمبود وزن'
        elif 14.7 <= bmi <= 17.2:
            return 'نرمال'
        elif 19.2 < bmi <= 24:
            return 'اضافه وزن'
        elif bmi > 24:
            return 'چاق'
    elif age == 12:
        if bmi < 15:
            return 'کمبود وزن'
        elif 15.1 <= bmi <= 20:
            return 'نرمال'
        elif 20.1 < bmi <= 25:
            return 'اضافه وزن'
        elif bmi > 25:
            return 'چاق'
    elif age == 13:
        if bmi < 15.1:
            return 'کمبود وزن'
        elif 15.2 <= bmi <= 20.8:
            return 'نرمال'
        elif 20.9 < bmi <=26.3 :
            return 'اضافه وزن'
        elif bmi > 26.3:
            return 'چاق'
    elif age == 14:
        if bmi < 15.8:
            return 'کمبود وزن'
        elif 15.8 <= bmi <= 20.4:
            return 'نرمال'
        elif 20.5 < bmi <= 27.3:
            return 'اضافه وزن'
        elif bmi > 27.3:
            return 'چاق'
    elif age == 15:
        if bmi < 16:
            return 'کمبود وزن'
        elif 16.1 <= bmi <= 22:
            return 'نرمال'
        elif 22.1 < bmi <= 28.3:
            return 'اضافه وزن'
        elif bmi > 28.3:
            return 'چاق'
    elif age == 16:
        if bmi < 16.3:
            return 'کمبود وزن'
        elif 16.4 <= bmi <= 22.8:
            return 'نرمال'
        elif 22.9 < bmi <= 29.3:
            return 'اضافه وزن'
        elif bmi > 29.3:
            return 'چاق'
    elif age == 17:
        if bmi < 17:
            return 'کمبود وزن'
        elif 17.1 <= bmi <= 23.1:
            return 'نرمال'
        elif 23.2 < bmi <= 30.3:
            return 'اضافه وزن'
        elif bmi > 30.3:
            return 'چاق'
    elif age == 18:
        if bmi < 17.4:
            return 'کمبود وزن'
        elif 17.5 <= bmi <= 23.5:
            return 'نرمال'
        elif 23.6 < bmi <= 31.3:
            return 'اضافه وزن'
        elif bmi > 31.3:
            return 'چاق'
    elif age == 19:
        if bmi < 17.8:
            return 'کمبود وزن'
        elif 17.8 <= bmi <= 24:
            return 'نرمال'
        elif 24.1 < bmi <= 31.5:
            return 'اضافه وزن'
        elif bmi > 31.5:
            return 'چاق'
    elif age == 20:
        if bmi < 18:
            return 'کمبود وزن'
        elif 18 <= bmi <= 24.3:
            return 'نرمال'
        elif 24.4 < bmi <= 32:
            return 'اضافه وزن'
        elif bmi > 32:
            return 'چاق'


# محاسبه توده بدنی آقا زیر 20 سال
def calculate_Body_boy_mass(bmi, age):
    if age == 2:
        if bmi < 15:
            return 'کمبود وزن'
        elif 15.1 <= bmi <= 17.8:
            return 'نرمال'
        elif 17.9 < bmi <= 19.1:
            return 'چاق'
    elif age == 3:
        if bmi < 14.5:
            return 'کمبود وزن'
        elif 14.6 <= bmi <= 17:
            return 'نرمال'
        elif 17.1 < bmi <= 18.4:
            return 'اضافه وزن'
        elif bmi > 18.4:
            return 'چاق'
    elif age == 4:
        if bmi < 14:
            return 'کمبود وزن'
        elif 14 <= bmi <= 16.8:
            return 'نرمال'
        elif 16.9 < bmi <= 18:
            return 'اضافه وزن'
        elif bmi > 18:
            return 'چاق'
    elif age == 5:
        if bmi < 14:
            return 'کمبود وزن'
        elif 14.1 <= bmi <= 16.4:
            return 'نرمال'
        elif 16.5 < bmi <= 18:
            return 'اضافه وزن'
        elif bmi > 18:
            return 'چاق'
    elif age == 6:
        if bmi < 13.8:
            return 'کمبود وزن'
        elif 13.9 <= bmi <= 16.4:
            return 'نرمال'
        elif 16.5 < bmi <= 18.6:
            return 'اضافه وزن'
        elif bmi > 18.7:
            return 'چاق'
    elif age == 7:
        if bmi < 13.8:
            return 'کمبود وزن'
        elif 13.9 <= bmi <= 16.8:
            return 'نرمال'
        elif 16.9 < bmi <= 19.4:
            return 'اضافه وزن'
        elif bmi > 19.4:
            return 'چاق'
    elif age == 8:
        if bmi < 13.8:
            return 'کمبود وزن'
        elif 13.9 <= bmi <= 17:
            return 'نرمال'
        elif 17.1 < bmi <= 20.4:
            return 'اضافه وزن'
        elif bmi > 20.4:
            return 'چاق'
    elif age == 9:
        if bmi < 14:
            return 'کمبود وزن'
        elif 14 <= bmi <= 17.6:
            return 'نرمال'
        elif 17.7 < bmi <= 21.4:
            return 'اضافه وزن'
        elif bmi > 21.4:
            return 'چاق'
    elif age == 10:
        if bmi < 14.4:
            return 'کمبود وزن'
        elif 14.5 <= bmi <= 18:
            return 'نرمال'
        elif 18.1 < bmi <= 22.3:
            return 'اضافه وزن'
        elif bmi > 22.4:
            return 'چاق'
    elif age == 11:
        if bmi < 14.6:
            return 'کمبود وزن'
        elif 14.7 <= bmi <= 19:
            return 'نرمال'
        elif 19.1 < bmi <= 22.8:
            return 'اضافه وزن'
        elif bmi > 22.8:
            return 'چاق'
    elif age == 12:
        if bmi < 15:
            return 'کمبود وزن'
        elif 15.1 <= bmi <= 19.5:
            return 'نرمال'
        elif 19.6 < bmi <= 24:
            return 'اضافه وزن'
        elif bmi > 24:
            return 'چاق'
    elif age == 13:
        if bmi < 15.4:
            return 'کمبود وزن'
        elif 15.5 <= bmi <= 20.4:
            return 'نرمال'
        elif 20.9 < bmi <=25 :
            return 'اضافه وزن'
        elif bmi > 25:
            return 'چاق'
    elif age == 14:
        if bmi < 16:
            return 'کمبود وزن'
        elif 16.1 <= bmi <= 21:
            return 'نرمال'
        elif 21.1< bmi <= 26:
            return 'اضافه وزن'
        elif bmi > 26:
            return 'چاق'
    elif age == 15:
        if bmi < 16.8:
            return 'کمبود وزن'
        elif 16.9 <= bmi <= 22:
            return 'نرمال'
        elif 22.1 < bmi <= 26.6:
            return 'اضافه وزن'
        elif bmi > 26.6:
            return 'چاق'
    elif age == 16:
        if bmi < 17:
            return 'کمبود وزن'
        elif 17.1 <= bmi <= 22.8:
            return 'نرمال'
        elif 22.9 < bmi <= 27.6:
            return 'اضافه وزن'
        elif bmi > 27.6:
            return 'چاق'
    elif age == 17:
        if bmi < 17.3:
            return 'کمبود وزن'
        elif 17.1 <= bmi <= 23.1:
            return 'نرمال'
        elif 23.2 < bmi <= 28.6:
            return 'اضافه وزن'
        elif bmi > 28.6:
            return 'چاق'
    elif age == 18:
        if bmi < 18:
            return 'کمبود وزن'
        elif 18.1 <= bmi <= 24:
            return 'نرمال'
        elif 24.1 < bmi <= 29:
            return 'اضافه وزن'
        elif bmi > 29:
            return 'چاق'
    elif age == 19:
        if bmi < 18.4:
            return 'کمبود وزن'
        elif 18.5 <= bmi <= 25:
            return 'نرمال'
        elif 24.1 < bmi <= 30:
            return 'اضافه وزن'
        elif bmi > 30:
            return 'چاق'
    elif age == 20:
        if bmi < 19:
            return 'کمبود وزن'
        elif 19 <= bmi <= 25.4:
            return 'نرمال'
        elif 25.5 < bmi <= 31.5:
            return 'اضافه وزن'
        elif bmi > 31.5:
            return 'چاق'



def contactFormView(request):
    issend = False
    user = User.objects.filter(id=request.user.id)
    if request.method == 'POST':
        formOn = forms.BMI_forms(request.POST)
        if formOn.is_valid():
            formOn.save()
            issend = True
            # محاسبه bmi
            height_m = formOn.cleaned_data.get('height')
            user.update(height=height_m)
            weight_kg = formOn.cleaned_data.get('weight')
            height_m = pow(height_m, 2)
            bmi = weight_kg / height_m
            user.update(weight=weight_kg)
            user.update(BMI_value=bmi)
            # شرایط محدوده سنی
            body_mass = ''
            if formOn.cleaned_data.get('age') >= 20:
                body_mass = calculate_Body_mass(bmi)
            elif formOn.cleaned_data.get('gender') == 'خانم' and formOn.cleaned_data.get('age') < 20:
                body_mass = calculate_Body_Girl_mass(bmi, formOn.cleaned_data.get('age'))
            elif formOn.cleaned_data.get('gender') == 'آقا' and formOn.cleaned_data.get('age') < 20:
                body_mass = calculate_Body_boy_mass(bmi, formOn.cleaned_data.get('age'))

            user.update(body_mass_user=body_mass)

            return redirect(reverse('Disease_group'))

    else:
        formOn = forms.BMI_forms()
    bmi = 0
    return render(request, 'computingBmi.html', {'form': formOn, 'issend': issend, 'bmi': bmi})


showFoods = []
listDisease = []


def Disease(request):
    user_user = User.objects.get(id=request.user.id)
    user_user.sickness.clear()
    dissease = models.DiseaseGroupModels.objects.all()
    dissease_cat = models.DiseaseGroupModels.objects.filter(caregory_id=None)
    if request.POST:
        if request.POST['tags-outside']:
            sub_sickness = (request.POST['tags-outside']).strip('][').split(',')
            for sub in sub_sickness:
                sub = json.loads(sub)
                sickness = sub.get('value')
                user_user.sickness.add(dissease.get(title__exact=sickness))
        if request.POST['tags-outside1']:
            category_sickness = (request.POST['tags-outside1']).strip('][').split(',')
            for category in category_sickness:
                category = json.loads(category)
                category = category.get('value')
                user_user.sickness.add(dissease.get(title__exact=category))
        user_user.save()
        return redirect(reverse('show_foods'))
    context = {
        'dissease': dissease,
        'dissease_cat': dissease_cat,
    }

    return render(request, 'dissease.html', context)


# نام این متوذ باید تغییر کنه
def show_food(request):
    user = User.objects.get(id=request.user.id)
    foods = models.FoodModels.objects.filter(Body_mass__title=user.body_mass_user.title())
    video_res = models.VideoResultModels.objects.filter(Body_mass__title=user.body_mass_user.title())
    comments = models.Comment.objects.filter(active_comment=True).order_by('-created_comment')[:3]
    if len(user.sickness.all()) > 0:
        showFoods = []
        for food in foods:
            for sickness_food in food.group.all():
                for sickness in user.sickness.all():
                    if sickness.title == sickness_food.title:
                        showFoods.append(food)
    else:
        showFoods = models.FoodModels.objects.filter(Body_mass__title=user.body_mass_user.title())


    sent = False
    new_comment = None
    if request.method == 'POST':
        comment_form = forms.commentsModelForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            sent = True
            new_comment.save()
    else:
        comment_form = forms.commentsModelForm()
    context = {
        'user': user,
        'foods': showFoods,
        'listDisease': listDisease,
        'video_res': video_res,
        'sent': sent,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'show_food.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="aplication/adminupload")
            response['Content_Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404
