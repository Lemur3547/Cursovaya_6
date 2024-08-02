import secrets
import string

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_confirm')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты на сервисе SendEmail перейдите по ссылке {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification_message(request):
    return render(request, 'users/email_verification_message.html')


def email_verification_token(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    login(request, user)
    return redirect(reverse('main:mailings'))


@login_required
def block_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(reverse('main:manager_view_user', kwargs={'pk': pk}))


class ResetPasswordView(TemplateView):
    def get(self, request):
        return render(request, 'users/reset_password.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            email = request.POST.get('email')
            alphabet = string.ascii_letters + string.digits
            new_password = ''.join(secrets.choice(alphabet) for i in range(20))
            user = User.objects.get(email=email)
            user.password = make_password(new_password, salt=None, hasher='default')
            user.save()
            send_mail(
                subject='Изменение пароля',
                message=f'Новый пароль для вашего аккаунта: {new_password}\n'
                        f'Никому не сообщайте ваши данные для входа в систему.\n\n'
                        f'Если вы не запрашивали новый пароль, игнорируйте данное сообщение.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
        return redirect(reverse('users:login'))
