# Generated by Django 5.0.7 on 2024-09-02 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('contacts', models.CharField(max_length=15)),
                ('amount_due', models.IntegerField()),
                ('sales_agent_name', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('produce_name', models.CharField(max_length=100)),
                ('produce_type', models.CharField(max_length=50)),
                ('tonnage', models.IntegerField()),
                ('dispatch_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_types', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_time', models.TimeField(auto_now_add=True)),
                ('stock_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_dealer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_price', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=0, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Groceryapp.stock')),
            ],
        ),
    ]