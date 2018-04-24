from django.core.management.base import BaseCommand
from myapp.management.commands.init_currencies import Command as InitCurrenciesCommand


INITILIZATION_COMMANDS = [
    InitCurrenciesCommand,
]


class Command(BaseCommand):
    """Group command to run other commands."""

    def handle(self, *args, **options):
        for command in INITILIZATION_COMMANDS:
            com = command()
            com.handle()
