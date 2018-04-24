from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from myapp.rest.serializers import ExchangeRateSerializer
from myapp.models import ExchangeRate
from myapp.utils import scrap_all_exchange_rates, scrap_exchange_rate


class ExchangeRateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows exchange rates to be viewed.
    """
    serializer_class = ExchangeRateSerializer

    def get_queryset(self):
        currency_short = self.kwargs.get('currency')
        if currency_short:
            currency_short = currency_short.upper()
            scrap_exchange_rate(currency_short)
            return ExchangeRate.objects.filter(currency__short_name=currency_short).order_by('-date')
        scrap_all_exchange_rates()
        return ExchangeRate.objects.all().order_by('-date')
