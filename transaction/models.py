from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from financial.models import Debt
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField(blank=True, default=0)
    total_commission = models.IntegerField(blank=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, null=True, blank=True)

    def formatted_total_amount(self):
        return '{:,.2f}'.format(self.total_amount)

    formatted_total_amount.admin_order_field = 'total_amount'  # Make it sortable in Django Admin

    def formatted_total_commission(self):
        return '{:,.2f}'.format(self.total_commission)
    formatted_total_commission.admin_order_field = 'total_commission'  

    def calculate_totals(self):
        total_amount = sum(item.quantity * item.product.price for item in self.transactiondetail_set.all()) or 0
        total_commission = sum(item.commission for item in self.transactiondetail_set.all())
        return total_amount, total_commission
    
    def save(self, *args, **kwargs):
        if not self.pk:  
            super().save(*args, **kwargs)
        else:
            self.total_amount, self.total_commission = self.calculate_totals()
            super().save(*args, **kwargs)


class TransactionDetail(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(blank=True, default=0)
    profit = models.IntegerField(blank=True, null=True, default=0)
    commission_percentage = models.DecimalField(max_digits=8, decimal_places=0, blank=True, default=0)
    commission = models.IntegerField(blank=True, null=True, default=0)

    def calculate_profit(self):
        cost_price = self.product.cost_price
        selling_price = self.product.price
        profit = (selling_price - cost_price) * self.quantity
        return profit

    def calculate_full_commission(self):
        profit = self.calculate_profit()
        commission = self.product.commission_percentage * profit
        return self.product.commission_percentage, commission
    
    def calculate_default_commission(self):
        profit = self.calculate_profit()
        commission = self.product.default_commission * profit
        return self.product.default_commission, commission
    
    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.profit = self.calculate_profit()
        if self.transaction.user.parent:
            self.commission_percentage, self.commission = self.calculate_full_commission()
        else:
            self.commission_percentage, self.commission = self.calculate_default_commission()

        super().save(*args, **kwargs)

        # Update or create Debt here
        debt_amount = self.quantity * self.price  # Adjust the logic based on your requirements
        
        if self.transaction.debt:
            # If Debt exists, update the amount
            self.transaction.debt.amount += debt_amount
            self.transaction.debt.save()
        else:
            # If Debt doesn't exist, create a new Debt
            debt = Debt.objects.create(customer=self.transaction.user, transaction=self.transaction, amount=debt_amount)
            self.transaction.debt = debt
            self.transaction.save()


    def __str__(self):
        return f"{self.transaction} - {self.product.name}"
    

@receiver(post_save, sender=TransactionDetail)
def update_transaction_totals(sender, instance, **kwargs):
    transaction = instance.transaction
    transaction.calculate_totals()
    transaction.save()
