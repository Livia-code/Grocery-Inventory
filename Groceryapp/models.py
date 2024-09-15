from django.db import models
from datetime import datetime

# Create your models here.
class Stock(models.Model):
    item_name = models.CharField(max_length=50, null=True, blank=True)
    stock_types = models.CharField(max_length=50, null=True, blank=True)
    stock_date = models.DateTimeField( auto_now_add = True, null= True, blank=True)
    stock_time =models.TimeField(auto_now_add=True)
    stock_quantity = models.IntegerField(default=0, null=True, blank=True)
    stock_cost = models.IntegerField(default=0, null=True, blank=True)
    stock_dealer_name = models.CharField(max_length=50, null=True, blank=True)
    stock_contact = models.CharField(max_length=50, null=True, blank=True)
    stock_branch_name = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.item_name
#We have created one class that suites a given table

class Sale(models.Model):
    #associating property item with the name of the stock being kept in the stock table/model.
    item = models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    def get_total(self):
    # Set default values to 0 if quantity or unit_price is None
        quantity = self.quantity if self.quantity is not None else 0
        unit_price = self.unit_price if self.unit_price is not None else 0
        total = quantity * unit_price
        return int(total)

    def get_change(self):
    # Ensure amount_received is not None, defaulting to 0 if it is
        amount_received = self.amount_received if self.amount_received is not None else 0
    
    # Get the total price
        total_price = self.get_total()
    
    # Calculate change
        change = amount_received - total_price
    
    # Return the absolute value of the change
        return abs(int(change))

    def _str_(self):
        return self.item.item_name
    

class CreditSale(models.Model):
    buyer_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contacts = models.CharField(max_length=15)
    amount_due = models.IntegerField()
    sales_agent_name = models.CharField(max_length=100)
    due_date = models.DateField()
    produce_name = models.CharField(max_length=100)
    produce_type = models.CharField(max_length=50)
    tonnage = models.IntegerField()
    dispatch_date = models.DateField()

    def __str__(self):
        return f"{self.buyer_name} - {self.produce_name} - {self.due_date}"
    
 




