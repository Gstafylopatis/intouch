from rest_framework.viewsets import ModelViewSet
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer


# Create your views here.
class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer