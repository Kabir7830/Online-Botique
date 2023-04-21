from django.contrib.auth import get_user_model
from django.db import models

from clothes.models import Clothes

User = get_user_model()


class Customers(User):
    class Meta:
        db_table = "customers"

    age = models.CharField(max_length=3)
    permanent_address = models.CharField(max_length=300)
    resident_address = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)


class Customer_Clothes(models.Model):
    class Meta:
        db_table = "customer_clothes"

    customer_id = models.ForeignKey(Customers, on_delete=models.RESTRICT)
    cothes_id = models.ForeignKey(Clothes, on_delete=models.RESTRICT)
    ordered_date = models.DateField()
    is_ordered = models.BooleanField(null=True, blank=True, default=False)


class Customer_Payment(models.Model):
    class Meta:
        db_table = "customer_payment"

    customer_clothes_id = models.ForeignKey(
        Customer_Clothes, on_delete=models.RESTRICT)
    total_amount = models.IntegerField()
    amount_paid = models.IntegerField()
    amount_left = models.IntegerField()
    discount = models.IntegerField()
    payment_date = models.DateField()


class Customer_Cart(models.Model):
    class Meta:
        db_table = "Customer_Cart"

    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Clothes, on_delete=models.PROTECT)


class Customer_Orders(models.Model):
    class Meta:
        db_table = "Customer_Orders"

    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Clothes, on_delete=models.RESTRICT)
    quantity = models.CharField(max_length=6)
    size = models.CharField(max_length=4)
    is_ordered = models.BooleanField(default=False, blank=True)


class Subscribe(models.Model):
    class Meta:
        db_table = "Subscribe"

    customer_mail = models.EmailField()
    joining_date = models.CharField(max_length=16, null=True, blank=True)
