from django.db import models


class ElectricShop(models.Model):
    ELECTRONIC_ITEMS = [("Mobile", "Mobile"), ("Laptop", "Laptop"), ("Watch", "Watch"), ("Tab", "Tab")]
    shop_owner = models.CharField(max_length=20)
    electronic_items = models.CharField(max_length=10, choices=ELECTRONIC_ITEMS)
    item_price = models.CharField(max_length=10)
    shop_address = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=20)
    customer_mobile_no = models.IntegerField()
    shop_opening_date = models.DateField()


