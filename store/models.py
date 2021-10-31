from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    phone2 = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    tax_id = models.CharField("AFM", max_length=15, blank=True)
    doy = models.CharField(max_length=100, blank=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=7,
                                     decimal_places=3,
                                     validators=[MinValueValidator(0)])

    purchase_price = models.DecimalField(max_digits=7,
                                         decimal_places=3,
                                         validators=[MinValueValidator(0)])

    inventory = models.DecimalField(
        max_digits=7,
        decimal_places=1,
    )

    last_update = models.DateTimeField(auto_now=True)


class Order(models.Model):

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_CHOICES = [(PAYMENT_STATUS_PENDING, 'Pending'),
                              (PAYMENT_STATUS_COMPLETE, 'Complete')]

    payment_status = models.CharField(max_length=1,
                                      choices=PAYMENT_STATUS_CHOICES,
                                      default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):

    order = models.ForeignKey(Order,
                              on_delete=models.PROTECT,
                              related_name='items')

    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='orderitems')

    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
