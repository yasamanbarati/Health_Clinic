from django import forms
from . import models


# class BMI_forms(forms.Form):
#     weight = forms.IntegerField(
#         label='وزن ',
#         widget=forms.NumberInput(attrs={'min': '0'}),
#         # validators=[
#         #     validators.MaxLengthValidator(100),
#         #     validators.EmailValidator,
#         # ]
#     )
#     height = forms.IntegerField(
#         label='قد ',
#         widget=forms.NumberInput(attrs={'min': '0'}),
#         # validators=[
#         #     validators.MaxLengthValidator(100),
#         #     validators.EmailValidator,
#         # ]
#     )
#     age = forms.IntegerField(
#         label='سن ',
#         widget=forms.NumberInput(attrs={'min': '10'}),
#         # validators=[
#         #     validators.MaxLengthValidator(100),
#         #     validators.EmailValidator,
#         # ]
#     )

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
                    'placeholder': 'قد را به سانتی متر وارد کنید',
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
