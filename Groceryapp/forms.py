from django.forms import ModelForm
from .models import Sale
from django import forms
from .models import CreditSale
from django.core.exceptions import ValidationError

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to']


class CreditSaleForm(forms.ModelForm):
    class Meta:
        model = CreditSale
        fields = ['produce_name', 'buyer_name', 'tonnage', 'national_id', 'contacts', 'location']