from django.shortcuts import render, redirect
from django.urls import reverse
from account_module.models import User
from . import forms
from . import models


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


# محاسبه توده بدنی آقا زیر 20 سال
def calculate_Body_boy_mass(bmi, age):
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
            weight_kg = formOn.cleaned_data.get('weight')
            height_m = pow(height_m, 2)
            bmi = weight_kg / height_m
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
    user = User.objects.get(id=request.user.id)
    dissease = models.DiseaseGroupModels.objects.all()
    global listDisease
    listDisease = []
    bmi = user.BMI_value
    if request.POST:
        listDisease = dict(request.POST).get('fav_language')
        return redirect(reverse('show_foods'))

    return render(request, 'dissease.html', {'dissease': dissease, 'bmi': bmi})


def show_food(request):
    foods = models.FoodModels.objects.all()
    user = User.objects.get(id=request.user.id)
    body_mass_user = user.body_mass_user
    # فیلتر غذا ها بر اساس  بیماری و توده بدنی کاربر
    global showFoods
    showFoods = []
    for poll in foods:
        if body_mass_user == poll.Body_mass.title:
            for choice in poll.group.all():
                for disease in listDisease:
                    if disease == choice.title:
                        showFoods.append(poll)
    context = {
        'food': foods,
        'listDisease': listDisease,
        'listFood': showFoods,
        'body_mass_user': body_mass_user
    }
    return render(request, 'show_food.html', context)

