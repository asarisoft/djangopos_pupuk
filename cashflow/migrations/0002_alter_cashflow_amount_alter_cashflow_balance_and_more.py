# Generated by Django 4.2.2 on 2023-06-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='expense',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='price',
            field=models.IntegerField(),
        ),
    ]
