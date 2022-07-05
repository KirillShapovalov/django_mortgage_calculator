from django.views.generic import ListView
from rest_framework import viewsets, status
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import MortgageOffer
from .serializers import MortgageOfferSerializer, CalculatePaymentSerializer
from .forms import CalculatorForm
from .utils import mortgage_calculator


class MortgageOfferViewSet(viewsets.ModelViewSet):
    """API"""
    queryset = MortgageOffer.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = MortgageOfferSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_fields = [
        'term_min',
        'term_max',
        'rate_min',
        'rate_max',
        'payment_min',
        'payment_max',
    ]
    ordering_fields = ['rate_min', ]

    def list(self, request, *args, **kwargs):
        price = request.query_params.get('price')
        deposit = request.query_params.get('deposit')
        term = request.query_params.get('term')
        ordering = request.query_params.get('ordering')
        if price and deposit and term:
            serializer = CalculatePaymentSerializer
            result = mortgage_calculator(int(price), int(deposit), int(term), api=True, ordering=ordering)
            return Response(serializer(result, many=True).data, status=status.HTTP_200_OK)
        else:
            queryset = MortgageOffer.objects.all()
            return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)


class OffersView(ListView):
    """Список предложений"""
    model = MortgageOffer
    queryset = MortgageOffer.objects.all()
    template_name = 'base.html'


def calculator(request):
    form = CalculatorForm()
    res = []
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            response = form.cleaned_data
            res = mortgage_calculator(
                response['price'],
                response['deposit'],
                response['term']
            )
        else:
            form = CalculatorForm()
    context = {
        'form': form,
        'offers': res
    }
    return render(request, 'calculator/calculator.html', context)
