from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('products', views.ProductViewSet)

urlpatterns = [path('', include(router.urls))]
