from rest_framework.routers import DefaultRouter
from .views import MortgageOfferViewSet


router = DefaultRouter()
router.register(r'offer', MortgageOfferViewSet, basename='offer')
# router.register(r'/', my_view, basename='index')
# urlpatterns += router.urls
