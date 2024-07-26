from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from main.models import Mailing, Client, Message, MailingLog


class MainPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'surname', 'patronymic', 'email', 'comment',)
    success_url = reverse_lazy('main:clients')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'surname', 'patronymic', 'email', 'comment',)
    success_url = reverse_lazy('main:clients')


class ClientsDetailView(DetailView):
    model = Client


class ClientsDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('main:clients')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('name', 'text',)
    success_url = reverse_lazy('main:messages')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('name', 'text',)
    success_url = reverse_lazy('main:messages')


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('main:messages')


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'first_mall', 'regularity', 'clients', 'message')
    success_url = reverse_lazy('main:mailings')

    def form_valid(self, form):
        mailing = form.save()
        if form.is_valid():
            mailing.status = 'created'
            mailing.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'first_mall', 'regularity', 'clients', 'message')
    success_url = reverse_lazy('main:mailings')


class MailingDetailView(DetailView):
    model = Mailing


@login_required
def mailing_set_status(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.status == 'active':
        mailing.status = 'completed'
    else:
        mailing.status = 'active'
    mailing.save()
    return redirect(reverse('main:view_mailing', kwargs={'pk': pk}))


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')


class MailingLogListView(ListView):
    model = MailingLog
    ordering = '-mailing_time'
