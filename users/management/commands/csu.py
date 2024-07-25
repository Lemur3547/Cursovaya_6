from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='Админ Великий',
            email='emikgal2507@gmail.com',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('Emik2507')
        user.save()
