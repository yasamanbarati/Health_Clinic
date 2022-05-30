from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from . import forms
from account_module.forms import RegisterForms, LoginForms, forgetpasswordForms, resetPasswordForms
from .models import User
from django.utils.crypto import get_random_string
from utils.email_service import send_email
from django.contrib.auth.hashers import make_password


class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        register_form = RegisterForms()
        return render(request, 'login_page.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            user_emial = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_emial).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است. ')
            else:
                if register_form.clean_confirm_password() == user_password:
                    new_user = User(
                        email=user_emial,
                        email_active_code=get_random_string(72),
                        is_active=False,
                        username=user_emial, )
                    new_user.set_password(user_password)
                    new_user.save()
                    send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user},
                               'activate_account.html')
                    return redirect(reverse('logIn_page'))

        return render(request, 'login_page.html', {'register_form': register_form})


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        login_form = LoginForms()
        context = {
            'loginForm': login_form
        }

        return render(request, 'login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email',
                                         'حساب کاربری شما فعال نشده است برای فعال سازی روی ایمیل ارسال شده کلیک کنید')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'loginForm': login_form
        }

        return render(request, 'login.html', context)


class ActiveAccountView(View):
    def get(self, request, activeCode):
        user: User = User.objects.filter(email_active_code__iexact=activeCode).first()
        if user is not None:
            if not user.is_active:
                user.email_active_code = get_random_string(74)
                user.is_active = True
                user.save()
                # todo: show success message to user
                return redirect(reverse('logIn_page'))
            else:
                # todo: show message your account was activated message to user
                pass

        raise Http404


class ForgetPassView(View):

    def get(self, request):
        forget_pass = forgetpasswordForms()
        is_send = False
        return render(request, 'ForgotPassword.html', {'forget_pass': forget_pass, 'is_send': is_send})

    def post(self, request):
        forget_pass = forgetpasswordForms(request.POST)
        is_send = False
        if forget_pass.is_valid():
            email_user = forget_pass.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email_user).first()
            if user is not None:
                is_send = True
                send_email('بازیابی رمز عبور', user.email, {'user': user}, 'forgot_pass_email.html')

        return render(request, 'ForgotPassword.html', {'forget_pass': forget_pass, 'is_send': is_send})


class ReesetPassView(View):

    def get(self, request, activeaccount):
        user: User = User.objects.filter(email_active_code__iexact=activeaccount).first()
        reset_pass = resetPasswordForms()
        is_error = False
        if user is None:
            return redirect(reverse('logIn_page'))
        print("def get")
        return render(request, 'reset_Pass.html', {'reset_pass': reset_pass, 'user': user, 'is_error': is_error})

    def post(self, request: HttpRequest, activeaccount):
        reset_pass = resetPasswordForms(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=activeaccount).first()
        is_error = False
        print("def post")
        if reset_pass.is_valid():
            if user is None:
                return redirect(reverse('logIn_page'))
            if reset_pass.clean_confirm_password() == reset_pass.cleaned_data.get('password'):
                user_new_pass = reset_pass.cleaned_data.get('password')
                user.set_password(user_new_pass)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                print("valid")
                return redirect(reverse('logIn_page'))
            else:
                print("notttttttttt valid")
                is_error = True

        return render(request, 'reset_Pass.html', {'reset_pass': reset_pass, 'user': user, 'is_error': is_error})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('logIn_page'))


# class CompleteRegisterView(CreateView):
#     form_class = forms.CompleteRegisterModelForm
#     template_name = 'contact_us_page.html'
#     success_url = '/register/'

class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        user = User.objects.filter(id=request.user.id).first()
        form = forms.CompleteRegisterModelForm(instance=user)
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'contact_us_page.html', context)

    def post(self, request: HttpRequest):
        user = User.objects.filter(id=request.user.id).first()
        form = forms.CompleteRegisterModelForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            print("this is_valid")
            user.save()
            form.save()
            return redirect(reverse('register_page'))

        context = {
            'user': user,
            'form': form
        }
        return render(request, 'contact_us_page.html', context)

# class EditUserProfilePage(View):
#     def get(self, request: HttpRequest):
#         current_user = User.objects.filter(id=request.user.id).first()
#         form = forms.CompleteRegisterModelForm()
#         context = {
#             'form': form,
#             'user': current_user
#         }
#         return render(request, 'contact_us_page.html', context)
#
#     def post(self, request: HttpRequest):
#         current_user = User.objects.filter(id=request.user.id).first()
#         edit_form = forms.CompleteRegisterModelForm(request.POST)
#         if edit_form.is_valid():
#             edit_form.save()
#             current_user.save()
#             return redirect(reverse('register_page'))
#         context = {
#             'form': edit_form,
#             'user': current_user
#         }
#         return render(request, 'contact_us_page.html', context)
