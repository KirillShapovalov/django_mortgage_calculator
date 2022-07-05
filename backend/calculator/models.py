from django.db import models


class MortgageOffer(models.Model):
    """Ипотечные предложения"""
    bank_name = models.CharField('Наименование банка', max_length=50, default='bank')
    term_min = models.IntegerField('Срок ипотеки, ОТ', default='10')
    term_max = models.IntegerField('Срок ипотеки, ДО', default='30')
    rate_min = models.FloatField('Ставка, ОТ', default=1.8)
    rate_max = models.FloatField('Ставка, ДО', default=9.8)
    payment_min = models.IntegerField('Сумма кредита, ОТ', default='1000000')
    payment_max = models.IntegerField('Сумма кредита, ДО', default='10000000')

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name = 'Ипотечное предложение'
        verbose_name_plural = 'Ипотечные предложения'
