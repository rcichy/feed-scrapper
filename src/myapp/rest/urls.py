from django.conf.urls import url, include
from myapp.rest import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('^exchange_rates/$', views.ExchangeRateViewSet.as_view({'get': 'list'})),
    url('^exchange_rates/by_currency/(?P<currency>.+)/$', views.ExchangeRateViewSet.as_view({'get': 'list'})),
]