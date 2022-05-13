from django import forms
from django.core import validators
from . import models


class RegisterForms(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': "text-md px-5",
            'placeholder': 'ایمیل',
        }),
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
        error_messages={'required': 'لطفا رمز عبور را وارد کنید'},
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
        error_messages={'required': 'لطفا رمز عبور را وارد کنید'},
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
        error_messages={'required': 'لطفا تکرار رمز عبور را وارد کنید'},
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
