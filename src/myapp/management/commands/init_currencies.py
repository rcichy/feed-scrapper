from django.core.management.base import BaseCommand
from myapp.models import Currency


DEFAULT_CURRENCIES = [
    'USD',
    'JPY',
    'BGN',
    'CZK',
    'DKK',
    'EEK',
    'GBP',
    'HUF',
    'PLN',
    'RON',
    'SEK',
    'CHF',
    'ISK',
    'NOK',
    'HRK',
    'RUB',
    'TRY',
    'AUD',
    'BRL',
    'CAD',
    'CNY',
    'HKD',
    'IDR',
    'INR',
    'KRW',
    'MXN',
    'MYR',
    'NZD',
    'PHP',
    'SGD',
    'THB',
    'ZAR',
]


class Command(BaseCommand):

    """Command to initialize myapp_currency table."""

    def handle(self, *args, **options):
        current_currencies = Currency.objects.all()
        if not current_currencies:
            for default_currency_short_name in DEFAULT_CURRENCIES:
                Currency.objects.create(short_name=default_currency_short_name)
        assert Currency.objects.count() == len(DEFAULT_CURRENCIES)
