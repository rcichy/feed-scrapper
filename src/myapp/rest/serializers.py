from rest_framework import serializers
from myapp.models import ExchangeRate, Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Currency
        fields = ('short_name')


class ExchangeRateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = ('currency', 'date', 'value')

    currency = serializers.SlugRelatedField(read_only=True, slug_field='short_name')
