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
        widgets = {
            'weight': forms.NumberInput(),
            'height': forms.NumberInput(),
            'age': forms.NumberInput(attrs={'min': '10'}),
            'gender': forms.RadioSelect(choices=Gender_choices)
        }
        labels = {
            'weight': 'وزن بر حسب کیلو گرم',
            'height': 'قد بر حسب متر',
            'age': 'سن',
            'gender': 'جنسیت'
        }
        error_messages = {

            'height': {
                'required': 'وارد کردن قد اجباری میباشد ,لطفا آن را وارد کنید.'
            },
            'weight': {
                'required': 'وارد کردن وزن اجباری میباشد ,لطفا آن را وارد کنید.'
            },
            'age': {
                'required': 'وارد کردن سن اجباری میباشد ,لطفا آن را وارد کنید.'
            },
            'gender': {'required': 'وارد کردن جنسیت اجباری میباشد ,لطفا آن را وارد کنید.'}

        }
