from .models import MortgageOffer
from operator import itemgetter


def mortgage_calculator(price, deposit, term, api=False, ordering=None):
    s = int(price - price * (deposit / 100))  # общая сумма кредита
    m = term * 12  # срок кредитования в месяцах
    offers = MortgageOffer.objects.filter(
        term_min__lte=term,
        term_max__gte=term,
        payment_min__lte=s,
        payment_max__gte=s,
    )
    resp = []
    for offer in offers:
        bank = offer.bank_name
        p_min = offer.rate_min  # минимальная месячная ставка по кредиту
        p_max = offer.rate_max  # максимальная месячная ставка по кредиту
        r_min = p_min / 12 / 100  # минимальная процентная ставка за год разделенная на 12 месяцев
        r_max = p_max / 12 / 100  # максимальная процентная ставка за год разделенная на 12 месяцев
        min_gen_rate = (1 + r_min) ** m  # минимальная общая процентная ставка
        max_gen_rate = (1 + r_max) ** m  # максимальная общая процентная ставка
        monthly_mortgage_payment_min = s * r_min * min_gen_rate / (
                min_gen_rate - 1)  # минимальный ежемесячный платеж по ипотеке
        monthly_mortgage_payment_max = s * r_max * max_gen_rate / (
                max_gen_rate - 1)  # максимальный ежемесячный платеж по ипотеке
        min_overpayment = monthly_mortgage_payment_min * m - s
        max_overpayment = monthly_mortgage_payment_max * m - s
        if api:
            res_offer = {
                "id": offer.id,
                "payment": int(monthly_mortgage_payment_min),
                "bank": bank,
                "term_min": offer.term_min,
                "term_max": offer.term_max,
                "rate_min": offer.rate_min,
                "rate_max": offer.rate_max,
                "payment_min": offer.payment_min,
                "payment_max": offer.payment_max
            }
        else:
            res_offer = {
                'bank': bank,
                'min_rate': p_min,
                'max_rate': p_max,
                'min_payment': int(monthly_mortgage_payment_min),
                'max_payment': int(monthly_mortgage_payment_max),
                'min_overpayment': int(min_overpayment),
                'max_overpayment': int(max_overpayment),
            }
        resp.append(res_offer)
    if ordering == 'rate_min':
        resp = sorted(resp, key=itemgetter('rate_min'))
    elif ordering == '-rate_min':
        resp = sorted(resp, key=itemgetter('rate_min'), reverse=True)
    return resp
