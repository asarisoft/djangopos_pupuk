# Generated by Django 4.2.2 on 2023-06-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_alter_transactiondetail_commission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='total_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total_commission',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='commission',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='commission_percentage',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='profit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]