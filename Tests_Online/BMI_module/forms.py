from django import forms
from . import models


class BMI_forms(forms.ModelForm):
    class Meta:
        model = models.BMIModels
        fields = ['weight', 'height', 'age', 'gender']
        Gender_choices = (
            ('آقا', 'آقا'),
            ('خانم', 'خانم')
        )

        # gender = forms.ChoiceField(choices=Gender_choices, widget=forms.RadioSelect)
        widgets = {
            'weight': forms.NumberInput(attrs={
                'class': 'form-control text-sm text-end w-100 bg-transparent  py-0 ps-4 pe-5 text-dark',
                'placeholder': 'وزن را به کیلوگرم وارد کنید',
                'max_value': '3',
                'validation': 'لطفا عدد وارد کنید',
            }
            ),
            'height': forms.NumberInput(
                attrs={
                    'class': 'form-control text-sm text-end w-100 bg-transparent  py-0 ps-4 pe-5 text-dark',
                    'placeholder': 'قد را به متر وارد کنید',
                    'max_value': '344',
                    'validation': 'لطفا عدد وارد کنید',
                }
            ),
            'age': forms.NumberInput(attrs={
                'min': '10',
                'class': 'form-control text-sm text-end w-100 bg-transparent  py-0 ps-4 pe-5 text-dark',
                'placeholder': 'سن خود را وارد کنید',
                'max_value': '80',
                'validation': 'لطفا عدد وارد کنید',
            }
            ),
            'gender': forms.RadioSelect(choices=Gender_choices, attrs={'class': 'mx-3 text-sm'})
        }
        # labels = {
        #     'weight': 'وزن بر حسب کیلو گرم',
        #     'height': 'قد بر حسب متر',
        #     'age': 'سن',
        #     'gender': 'جنسیت'
        # }
        error_messages = {

            'height': {
                'required': 'وارد کردن قد اجباری میباشد ,لطفا آن را وارد کنید',
            },
            'weight': {
                'required': 'وارد کردن وزن اجباری میباشد ,لطفا آن را وارد کنید',
            },
            'age': {
                'required': 'وارد کردن سن اجباری میباشد ,لطفا آن را وارد کنید'
            },
            'gender': {'required': 'وارد کردن جنسیت اجباری میباشد ,لطفا آن را وارد کنید'}
        }


class commentsModelForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text_comment']
        widgets = {
            'text_comment': forms.TextInput()
        }
        labels = {
            'text_comment': 'متن نظر شما'
        }
        error_messages = {
            'text_comment': {
                'required': 'لطفا نظر خود را وارد کنید.'
            }
        }

# sub_choiceCategory = {}
# for sickness_sub in models.DiseaseGroupModels.objects.filter(caregory_id=None):
#     for sickness in sickness_sub.diseasegroupmodels_set.all:
#         sub_choiceCategory[sickness] = sickness
# sub_choiceCategory = list(sub_choiceCategory.items())
# sub_choiceCategory = tuple(sub_choiceCategory)

# class sicknessForm(forms.Form):
#     ChoiceList_category = {}
#     for item in models.DiseaseGroupModels.objects.filter(caregory_id=None):
#         ChoiceList_category[item] = item
#     ChoiceList_category = list(ChoiceList_category.items())
#     ChoiceList_category = tuple(ChoiceList_category)
#     item = forms.ChoiceField(choices=ChoiceList_category)
