from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from blog.models import Post
from main.forms import MailingForm, ClientForm, MessageForm
from main.models import Mailing, Client, Message, MailingLog
from users.models import User


class MainPage(TemplateView):
    """Контроллер для главной страницы"""
    def get(self, request, *args, **kwargs):
        context = {
            'mailings_count': Mailing.objects.all().count(),
            'active_mailings': Mailing.objects.filter(status='active', is_active=True).count(),
            'clients': Client.objects.all().distinct('email').count(),
            'blog': Post.objects.all().order_by('-created_at')[:3]
        }
        return render(request, 'main/index.html', context)


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер для страницы со списком клиентов"""
    model = Client

    def get_queryset(self, *args, **kwargs):
        # Получение списка клиентов принадлежащих текущему пользователю
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients')

    def form_valid(self, form):
        # Привязка текущего пользователя к создаваемому клиенту
        client = form.save()
        client.user = self.request.user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients')

    def get_form_class(self):
        # Ограничение доступа для других пользователей
        user = self.request.user
        if user == self.object.user:
            return ClientForm
        raise PermissionDenied


class ClientsDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра клиента"""
    model = Client

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления клиента"""
    model = Client
    success_url = reverse_lazy('main:clients')

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер для страницы со списком писем"""
    model = Message

    def get_queryset(self, *args, **kwargs):
        # Получение списка писем принадлежащих текущему пользователю
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания письма"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:messages')

    def form_valid(self, form):
        # Привязка текущего пользователя к создаваемому письму
        message = form.save()
        message.user = self.request.user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения письма"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:messages')

    def get_form_class(self):
        # Ограничение доступа для других пользователей
        user = self.request.user
        if user == self.object.user:
            return MessageForm
        raise PermissionDenied


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра письма"""
    model = Message

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления письма"""
    model = Message
    success_url = reverse_lazy('main:messages')

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MailingListView(LoginRequiredMixin, ListView):
    """Контроллер для страницы со списком рассылок"""
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        # Получение списка рассылок принадлежащих текущему пользователю
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailings')

    def form_valid(self, form):
        # Установление статуса рассылки на "создана"
        # Привязка текущего пользователя к создаваемой рассылке
        mailing = form.save()
        if form.is_valid():
            mailing.status = 'created'
            mailing.save()
        mailing.user = self.request.user
        mailing.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MailingCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailings')

    def get_form_class(self):
        # Ограничение доступа для других пользователей
        user = self.request.user
        if user == self.object.user:
            return MailingForm
        raise PermissionDenied

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied

    def get_form_kwargs(self):
        kwargs = super(MailingUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра рассылки"""
    model = Mailing

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied



@login_required
def mailing_set_status(request, pk):
    """Контроллер для завершения и возобновления рассылки"""
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.status == 'active':
        mailing.status = 'completed'
    else:
        mailing.status = 'active'
    mailing.save()
    return redirect(reverse('main:view_mailing', kwargs={'pk': pk}))


@login_required
def disable_mailing(request, pk):
    """Контроллер для отключения рассылки менеджером"""
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True
    mailing.save()
    return redirect(reverse('main:manager_view_mailing', kwargs={'pk': pk}))


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('main:mailings')

    def get_object(self, queryset=None):
        # Ограничение доступа для других пользователей
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MailingLogListView(LoginRequiredMixin, ListView):
    """Контроллер для страницы со списком отчетов по рассылкам"""
    model = MailingLog
    ordering = '-mailing_time'

    def get_queryset(self, *args, **kwargs):
        # Получение списка отчетов принадлежащих текущему пользователю
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ManagerMailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Контроллер для страницы со списком рассылок для менеджера"""
    model = Mailing
    template_name = 'main/manager_mailing_list.html'
    permission_required = 'main.view_mailing'


class ManagerMailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Контроллер для просмотра рассылки для менеджера"""
    model = Mailing
    template_name = 'main/manager_mailing_detail.html'
    permission_required = 'main.view_mailing'


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Контроллер для страницы со списком пользователей"""
    model = User
    permission_required = 'users.view_user'


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Контроллер для просмотра пользователя"""
    model = User
    permission_required = 'users.view_user'

    def get_context_data(self, **kwargs):
        # Получение данных о пользователе
        context_data = super().get_context_data(**kwargs)
        context_data['user'] = self.request.user
        context_data['viewable_user'] = User.objects.get(pk=self.kwargs['pk'])
        return context_data
