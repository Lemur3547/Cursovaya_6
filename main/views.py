from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from main.models import Mailing, Client


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


# Create your views here.
