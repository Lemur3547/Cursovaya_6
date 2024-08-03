from django.core.management import BaseCommand

from main.send_email import time_check


class Command(BaseCommand):
    def handle(self, *args, **options):
        time_check()
