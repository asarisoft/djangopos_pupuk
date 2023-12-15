# Generated by Django 4.2.2 on 2023-12-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0005_debt_remaining_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='debt',
            name='amount_paid',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='debt',
            name='remaining_amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]