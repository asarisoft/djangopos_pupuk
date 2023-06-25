from django.db import models

class CashFlow(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    income = models.IntegerField()
    expense = models.IntegerField()
    balance = models.IntegerField()


    def save(self, *args, **kwargs):
        # Update balance when the CashFlow object is saved
        if self.pk is None:
            # New object, add the income to the previous balance
            self.balance = self.income - self.expense
        else:
            # Existing object, calculate the difference between the amount and the previous balance
            difference = self.amount - CashFlow.objects.get(pk=self.pk).amount
            self.balance += difference

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.description}"