from django.db import models
from django.utils import timezone
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class ExchangeRate(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    id = models.CharField(max_length=6, primary_key=True)
    currency_a = models.CharField(max_length=3)
    currency_b = models.CharField(max_length=3)
    buy = models.DecimalField(max_digits=8, decimal_places=2)
    sell = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)

    def to_dict(self):
        currency_a = self.currency_a.lower()
        return {
            f'{currency_a}_buy': self.buy,
            f'{currency_a}_sell': self.sell
        }
