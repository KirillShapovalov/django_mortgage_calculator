from django import forms
from .models import MortgageOffer
from django.db.models import Max

max_term = MortgageOffer.objects.aggregate(Max('term_max')).get('term_max__max')


class CalculatorForm(forms.Form):
    price = forms.IntegerField(
        label='Стоимость объекта недвижимости, в рублях без копеек',
        required=True
    )
    deposit = forms.FloatField(
        label='Первоначальный взнос, в процентах',
        required=True,
        max_value=100
    )
    term = forms.IntegerField(
        label='Срок, в годах',
        max_value=max_term,
        required=True,
    )
