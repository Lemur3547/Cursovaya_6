from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from main.models import Mailing, Client, Message


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
    fields = ('name', 'first_mall', 'regularity', 'status', 'clients', 'message')
    success_url = reverse_lazy('main:index')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'first_mall', 'regularity', 'status', 'clients', 'message')
    success_url = reverse_lazy('main:index')


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:index')
