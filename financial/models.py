from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Debt(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    due_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    def update_status(self):
        self.remaining_amount = max(0, self.amount - self.amount_paid)
        if self.remaining_amount == 0:
            self.is_paid = True
        else:
            self.is_paid = False

    def save(self, *args, **kwargs):
        self.update_status()  # Update status before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.full_name} - {self.amount} - {self.remaining_amount} - {self.is_paid}"


class Payment(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    payment_date = models.DateField()
    description = models.TextField(blank=True, null=True)


@receiver(post_save, sender=Payment)
def update_debt_on_payment_save(sender, instance, **kwargs):
    # Update Debt when Payment is saved
    debt = instance.debt
    debt.amount_paid += instance.amount
    debt.save()
