from celery import shared_task
from celery.worker.state import requests

from LMS.settings import EXCHANGE_RATES_SOURCE
from exchanger.models import ExchangeRate


CURRENCY_MAP = [
    'UAH',
    'USD',
    'EUR',
    'RUB',
]


@shared_task
def get_exchange_rates():
    resp = requests.get(EXCHANGE_RATES_SOURCE)
    resp = resp.json()
    exchange_rates = [get_exchange_rate(d) for d in filter_out_rates(resp)]
    ExchangeRate.objects.all().delete()
    ExchangeRate.objects.bulk_update_or_create(exchange_rates, match_field=id)


def filter_out_rates(rates):
    for r in rates:
        currency_a = r['baseCurrency']
        if currency_a not in CURRENCY_MAP:
            continue
        currency_b = r['currency']
        if r['currency'] not in CURRENCY_MAP:
            continue
        if currency_a != 'UAH' and currency_b != 'UAH':
            continue
        r['currency_a'] = CURRENCY_MAP[currency_a]
        r['currency_b'] = CURRENCY_MAP[currency_b]
        yield r


def get_exchange_rate(rate):
    currency_a = rate['currency_a']
    currency_b = rate['currency_b']
    return ExchangeRate(
        id=currency_a + currency_b,
        currency_a=currency_a,
        currency_b=currency_b,
        buy=rate['purchaseRateNB'],
        sell=rate['saleRateNB']
    )
