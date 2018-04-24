from django.db import models

# Create your models here.


class Currency(models.Model):
    """Model for currencies."""
    short_name = models.CharField("Short name", max_length=3)  # ex. "USD"


class ExchangeRate(models.Model):
    """This model holds scraped exchange rates."""
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=4, max_digits=12)
    date = models.DateField()

