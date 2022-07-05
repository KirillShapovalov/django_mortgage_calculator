from rest_framework import serializers
from .models import MortgageOffer


class MortgageOfferSerializer(serializers.ModelSerializer):
    """
    Список ипотечных предложений
    """
    bank_name = serializers.CharField(max_length=50)
    # payment = serializers.IntegerField(default=0)
    term_min = serializers.IntegerField(default=10)
    term_max = serializers.IntegerField(default=30)
    rate_min = serializers.FloatField(default=1.8)
    rate_max = serializers.FloatField(default=9.8)
    payment_min = serializers.IntegerField(default=1000000)
    payment_max = serializers.IntegerField(default=10000000)

    class Meta:
        model = MortgageOffer
        fields = '__all__'

    def create(self, validated_data):
        return MortgageOffer.objects.create(**validated_data)


class CalculatePaymentSerializer(serializers.Serializer):
    """
    Расчет платежа
    """
    id = serializers.IntegerField(default=0)
    payment = serializers.IntegerField(default=0)
    bank = serializers.CharField(max_length=50)
    term_min = serializers.IntegerField(default=10)
    term_max = serializers.IntegerField(default=30)
    rate_min = serializers.FloatField(default=1.8)
    rate_max = serializers.FloatField(default=9.8)
    payment_min = serializers.IntegerField(default=1000000)
    payment_max = serializers.IntegerField(default=10000000)
