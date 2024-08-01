from django.urls import path

from main.views import ClientListView, ClientCreateView, ClientUpdateView, ClientsDetailView, ClientsDeleteView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, MailingLogListView, \
    mailing_set_status, MainPage, ManagerMailingListView, UserListView, ManagerMailingDetailView, disable_mailing, \
    UserDetailView
from users.views import block_user

urlpatterns = [
    path('', MainPage.as_view(), name='index'),

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

    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('add_mailing/', MailingCreateView.as_view(), name='add_mailing'),
    path('edit_mailing/<int:pk>', MailingUpdateView.as_view(), name='edit_mailing'),
    path('view_mailing/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('delete_mailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),

    path('mailing_logs/', MailingLogListView.as_view(), name='mailing_logs'),
    path('set_status/<int:pk>', mailing_set_status, name='mailing_set_status'),
    path('disable_mailing/<int:pk>', disable_mailing, name='disable_mailing'),
    path('block_user/<int:pk>', block_user, name='block_user'),

    path('manager/mailings/', ManagerMailingListView.as_view(), name='manager_mailings'),
    path('manager/view_mailing/<int:pk>', ManagerMailingDetailView.as_view(), name='manager_view_mailing'),
    path('manager/users/', UserListView.as_view(), name='manager_users'),
    path('manager/user/<int:pk>', UserDetailView.as_view(), name='manager_view_user'),
]
