from django.db import models

# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    phone2 = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    tax_number = models.CharField("AFM", max_length=15, blank=True)
    doy = models.CharField(max_length=100, blank=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
