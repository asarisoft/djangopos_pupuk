# Generated by Django 4.2.2 on 2023-06-18 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_commission', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('profit', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('commission_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('commission', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
    ]
