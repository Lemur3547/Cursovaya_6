from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from main.forms import MailingForm, ClientForm, MessageForm
from main.models import Mailing, Client, Message, MailingLog


class MainPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients')

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return ClientForm
        raise PermissionDenied


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('main:clients')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:messages')

    def form_valid(self, form):
        message = form.save()
        message.user = self.request.user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:messages')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return MessageForm
        raise PermissionDenied


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('main:messages')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailings')

    def form_valid(self, form):
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
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailings')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return MailingForm
        raise PermissionDenied

    def get_object(self, queryset=None):
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
    model = Mailing

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied



@login_required
def mailing_set_status(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.status == 'active':
        mailing.status = 'completed'
    else:
        mailing.status = 'active'
    mailing.save()
    return redirect(reverse('main:view_mailing', kwargs={'pk': pk}))


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user == self.object.user:
            return self.object
        raise PermissionDenied


class MailingLogListView(LoginRequiredMixin, ListView):
    model = MailingLog
    ordering = '-mailing_time'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset
