from dataclasses import fields
from email import message
from re import M
from django import forms
from django.core import validators
from . import models
from .models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterForms(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': "text-md px-5",
            'placeholder': 'ایمیل',
        }),
        error_messages={'required': 'لطفا ایمیل را وارد کنید'},
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': "text-md px-5",
                'placeholder': 'رمز عبور',
            }
        ),
        min_length=6,
        error_messages={'required': 'لطفا تکرار رمز عبور را وارد کنید',
                        'min_length': 'رمز عبور شما باید حداقل 6 کاراکتر باشد',
                        },

        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    comfirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': "text-md px-5",
                'placeholder': 'تکرار رمز عبور',
            }
        ),
        error_messages={'required': 'لطفا تکرار رمز عبور را وارد کنید'},

        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        comfirm_password = self.cleaned_data.get('comfirm_password')
        if password != comfirm_password:
            self.add_error('comfirm_password', "رمز عبور و تکرار رمز عبور با یک دیگر مغایرت ندارند")
        else:
            return comfirm_password


    # def clean_confirm_password(self):
    #     passwords=self.cleaned_data.get('passwords')
    #     confirm_passwords=self.cleaned_data.get('comfirm_passwords')
    #     if passwords == confirm_passwords:
    #         return confirm_passwords
    #     else:
    #         raise ValidationError('رمز عبور با تکرار رمز عبور مغایرت ندارد')


class LoginForms(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': "text-md px-5",
            'placeholder': 'ایمیل',
        }),
        required=True,
        error_messages={'required': 'لطفا ایمیل را وارد کنید'},
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': "text-md px-5",
                'placeholder': 'رمز عبور',
            }
        ),

        required=True,
        min_length=6,
        error_messages={'required': 'لطفا رمز عبور را وارد کنید'
                        },
        validators=[
            validators.MaxLengthValidator(100),

        ]
    )


class forgetpasswordForms(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': "text-md px-5",
            'id': "email-phone",
            'placeholder': 'ایمیل',
        }),

        required=True,
        error_messages={'required': 'لطفا ایمیل را وارد کنید'
                        },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )


class resetPasswordForms(forms.Form):
    password = forms.CharField(
        label='رمز عبور',

        widget=forms.PasswordInput(
            attrs={
                'class': "text-md px-5",
                'placeholder': 'رمز عبور',
            }
        ),

        validators=[
            validators.MaxLengthValidator(100)
        ],
        required=True,
        min_length=6,
        error_messages={'required': 'لطفا تکرار رمز عبور را وارد کنید',
                        'min_length': 'رمز عبور شما باید حداقل 6 کاراکتر باشد'},
    )
    comfirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': "text-md px-5",
                'placeholder': 'تکرار رمز عبور',
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ],
        required=True,
        min_length=6,
        error_messages={'required': 'لطفا تکرار رمز عبور را وارد کنید',
                        'min_length': 'رمز عبور شما باید حداقل 6 کاراکتر باشد'},
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        comfirm_password = self.cleaned_data.get('comfirm_password')
        if password != comfirm_password:
            self.add_error('comfirm_password', "رمز عبور و تکرار رمز عبور با یک دیگر مغایرت ندارند")
        else:
            return comfirm_password


    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get('password')
    #     comfirm_password = self.cleaned_data.get('comfirm_password')
    #     if password != comfirm_password:
    #         self.add_error('comfirm_password', "Password does not match")
    #     else:
    #         return comfirm_password


class CompleteRegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'users_name', 'weight', 'height', 'about_text', 'avatar']
        widgets = {
            'users_name': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'weight': forms.NumberInput(attrs={'min': '0'}),
            'height': forms.NumberInput(attrs={'min': '0'}),
            'about_text': forms.Textarea(),
            'avatar': forms.FileInput(),
        }
        labels = {
            'users_name': 'ایدی',
            'first_name': 'نام',
            'last_name': 'نام و نام خانوادگی ',
            'weight': 'وزن',
            'height': 'قد',
            'about_text': 'توضیحات در باره خود (اختیاری)',
            'avatar': 'تصویر آواتار'
        }
        # error_messages = {
        #     'first_name': {
        #         'required': 'نام و نام خانوادگی اجباری میباشد ,لطفا آن را وارد کنید.'
        #     },
        #     'last_name': {
        #         'required': 'ایمیل اجباری میباشد ,لطفا آن را وارد کنید.'
        #     },
        #     'user_name': {
        #         'required': '',
        #     },
        #     'height': {
        #         'required': 'وارد کردن قد اجباری میباشد ,لطفا آن را وارد کنید.'
        #     },
        #     'weight': {
        #         'required': 'وارد کردن وزن اجباری میباشد ,لطفا آن را وارد کنید.'
        #     }
        # 'about_text': {
        #     'required': 'متن شما اجباری میباشد ,لطفا آن را وارد کنید.'
        # },
        #
        # }


class EditPanelModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditPanelModelForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control text-sm text-end w-100 bg-transparent py-0 ps-4 pe-5 text-dark',
                'placeholder': 'نام  خود را وارد کنید',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control text-sm text-end w-100 bg-transparent py-0 ps-4 pe-5 text-dark',
                'placeholder': 'نام خود را وارد کنید',
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control text-sm text-end w-100 bg-transparent py-0 ps-4 pe-5 text-dark',
                'placeholder': 'ایمیل خود را وارد کنید',
            }),
        }
        labels = {
            'first_name': 'نام ',
            'last_name': ' نام خانوادگی ',
            'email': 'ایمیل',
        }

        error_messages = {
            'first_name': {
                'required': 'نام اجباری میباشد ,لطفا آن را وارد کنید.'
            },
            'last_name': {
                'required': 'نام خانوادگی اجباری میباشد ,لطفا آن را وارد کنید.'
            },
            'email': {
                'required': 'ایمیل اجباری میباشد ,لطفا آن را وارد کنید.'
            },
        }


class UpdateprofileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.form_request = kwargs.pop("request", None)
        super(UpdateprofileForm, self).__init__(*args, **kwargs)



        GENDER_CHOICES = [
            ('male', "مرد"),
            ('female', "زن")
            ]

        if self.form_request.method == 'POST':
            self.fields['first_name'] = forms.CharField(max_length=100, initial=self.form_request.POST.get('first_name'), required=True, error_messages={'required': 'نام اجباری میباشد ,لطفا آن را وارد کنید.'})
            self.fields['last_name'] = forms.CharField(max_length=100, initial=self.form_request.POST.get('last_name'), required=True, error_messages={'required': 'نام خانوادگی اجباری میباشد ,لطفا آن را وارد کنید.'})
            self.fields['email'] = forms.EmailField(initial=self.form_request.POST.get('email'), disabled=True)
            self.fields['phonenumber'] = forms.CharField(max_length=16, initial=self.form_request.POST.get('phonenumber'), required=False)
            self.fields['age'] = forms.CharField(initial=self.form_request.POST.get('age'), required=False)
            self.fields['gender'] = forms.ChoiceField(initial=self.form_request.POST.get('gender'), required=True, widget=forms.RadioSelect, choices=GENDER_CHOICES)
            self.fields['weight'] = forms.CharField(initial=self.form_request.POST.get('weight'), required=False)
        else:
            self.fields['first_name'] = forms.CharField(max_length=100, initial=self.form_request.user.first_name, required=True, error_messages={'required': 'نام اجباری میباشد ,لطفا آن را وارد کنید.'})
            self.fields['last_name'] = forms.CharField(max_length=100, initial=self.form_request.user.last_name, required=True, error_messages={'required': 'نام خانوادگی اجباری میباشد ,لطفا آن را وارد کنید.'})
            self.fields['email'] = forms.EmailField(initial=self.form_request.user.email, disabled=True)
            self.fields['phonenumber'] = forms.CharField(max_length=16, initial=self.form_request.user.phonenumber, required=False)
            self.fields['age'] = forms.CharField(initial=self.form_request.user.age, required=False)
            self.fields['gender'] = forms.ChoiceField(initial=self.form_request.user.gender, required=True, widget=forms.RadioSelect, choices=GENDER_CHOICES)
            self.fields['weight'] = forms.CharField(initial=self.form_request.user.weight, required=False)


    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'phonenumber', 'age', 'avatar', 'gender', 'weight']



    def convert_to_english(input):
        num_dict = {
            '۰' : '0',
            '۱' : '1',
            '۲' : '2',
            '۳' : '3',
            '۴' : '4',
            '۵' : '5',
            '۶' : '6',
            '۷' : '7',
            '۸' : '8',
            '۹' : '9'
        }

        for p, e in num_dict.items():
            input = input.replace(p, e)
        return input  


    def clean_phonenumber(self):
        cleaned_data = super(UpdateprofileForm, self).clean()
        phonenumber = cleaned_data.get('phonenumber')
        phonenumber = UpdateprofileForm.convert_to_english(phonenumber)

        if len(phonenumber) != 0:
            if str.isdigit(phonenumber):
                if len(phonenumber) != 11:
                    raise forms.ValidationError([{'phonenumber' : 'طول شماره باید ۱۱ کاراکتر باشد.'}]) 


                try:
                    RegexValidator(regex = r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}")
                except ValidationError:
                    raise forms.ValidationError([{'phonenumber' : 'شماره نامعتبر است.'}]) 


                try:
                    User.objects.get(phonenumber=phonenumber)
                except User.DoesNotExist:
                    return phonenumber
                else:
                    if self.form_request.user.phonenumber == phonenumber:
                        return phonenumber
                raise forms.ValidationError([{'phonenumber' : 'شماره مورد نظر درحال استفاده است.'}])
            else:
                raise ValidationError([{'phonenumber' : 'داده ورودی برای شماره تملس از نوع عدد نیست. لطفا فقط عدد وارد کنید'}])

          


    def clean_age(self):
        cleaned_data = super(UpdateprofileForm, self).clean()
        age = cleaned_data.get('age')
        age = UpdateprofileForm.convert_to_english(age)


        if len(str(age)) != 0:

            if str.isdigit(age):

                Integer_age = int(age)
                if Integer_age < 0:
                    raise ValidationError([{'age' : 'سن وارد شده کمتر از حد مجاز است.'}])

                if Integer_age > 100:
                    raise ValidationError([{'age' : 'سن وارد شده بیشتر از حد مجاز است.'}])

                else:
                    return age

            else:
                raise ValidationError([{'age' : 'داده ورودی از نوع عدد نیست. لطفا فقط عدد وارد کنید'}])




    def clean_weight(self):
        cleaned_data = super(UpdateprofileForm, self).clean()
        weight = cleaned_data.get('weight')
        weight = UpdateprofileForm.convert_to_english(weight)


        if len(weight) != 0:
                if str.isdigit(weight):
                    if float(weight) < 350 and float(weight) > 0:
                        return weight
                    else:
                        raise ValidationError([{'weight' : 'وزن وارد شده خارج از محدوده مجاز است'}])
                else:
                    raise ValidationError([{'weight' : 'داده ورودی از نوع عدد نیست. لطفا فقط عدد وارد کنید'}])



