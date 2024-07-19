from django.urls import path

from main.views import ClientListView, ClientCreateView, ClientUpdateView, ClientsDetailView, ClientsDeleteView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, MailingLogListView, \
    mailing_set_status

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='clients'),
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('view_client/<int:pk>', ClientsDetailView.as_view(), name='view_client'),
    path('delete_client/<int:pk>', ClientsDeleteView.as_view(), name='delete_client'),

    path('messages/', MessageListView.as_view(), name='messages'),
    path('add_message/', MessageCreateView.as_view(), name='add_message'),
    path('edit_message/<int:pk>', MessageUpdateView.as_view(), name='edit_message'),
    path('view_message/<int:pk>', MessageDetailView.as_view(), name='view_message'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),

    path('', MailingListView.as_view(), name='index'),
    path('add_mailing/', MailingCreateView.as_view(), name='add_mailing'),
    path('edit_mailing/<int:pk>', MailingUpdateView.as_view(), name='edit_mailing'),
    path('view_mailing/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('delete_mailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),

    path('mailing_logs/', MailingLogListView.as_view(), name='mailing_logs'),
    path('set_status/<int:pk>', mailing_set_status, name='mailing_set_status')
]
