from django.urls import path

from . import views

urlpatterns = [
    # path('offer/', views.MortgageOfferViewSet.as_view()),
    path('', views.OffersView.as_view(), name='offers'),
    path('calculator/', views.calculator, name='calculator'),
]
