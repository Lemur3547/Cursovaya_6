from django.urls import path

from main.views import ClientListView, ClientCreateView, ClientUpdateView, ClientsDetailView, ClientsDeleteView, \
    MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='clients'),
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('view_client/<int:pk>', ClientsDetailView.as_view(), name='view_client'),
    path('delete_client/<int:pk>', ClientsDeleteView.as_view(), name='delete_client'),

]
