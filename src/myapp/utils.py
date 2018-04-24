import datetime
from decimal import Decimal
from django.conf import settings
import feedparser
from time import mktime

from myapp.models import ExchangeRate, Currency


def get_currency(currency):
    """Return Currency object from string short name."""
    if isinstance(currency, Currency):
        return currency
    return Currency.objects.filter(short_name=currency.upper()).first()


def scrap_exchange_rate(currency, update=False, force=False):
    currency = get_currency(currency)
    today = datetime.date.today()
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    if not force and \
            ExchangeRate.objects.filter(currency=currency).exists() and \
            ExchangeRate.objects.filter(currency=currency).latest('date').date in (today, yesterday):
        # skip scraping if have latest data in database
        # new exchange rates are anounced in the middle of a day
        return

    url = settings.RSS_URL.format(currency.short_name.lower())
    feed = feedparser.parse(url)
    for entry in feed['entries']:
        value = Decimal(entry['cb_exchangerate'].split()[0])
        date = datetime.datetime.fromtimestamp(mktime(entry['updated_parsed'])).date()
        exchange_rate = ExchangeRate.objects.filter(currency=currency, date=date).first()
        if update and exchange_rate:
            exchange_rate.value = value
            exchange_rate.save()
        elif not exchange_rate:
            ExchangeRate.objects.create(currency=currency, date=date, value=value)


def scrap_all_exchange_rates():
    for currency in Currency.objects.all():
        scrap_exchange_rate(currency)


def get_exchange_rate(currency, date):
    currency = get_currency(currency)
    query = dict(currency=currency, date=date)
    if not ExchangeRate.objects.filter(**query).exists():
        scrap_exchange_rate(currency)
    return ExchangeRate.objects.filter(**query).first()
