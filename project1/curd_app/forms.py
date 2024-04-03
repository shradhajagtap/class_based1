from django import forms

from .models import ElectricShop


class ElectricShopForm(forms.ModelForm):
    class Meta:
        model = ElectricShop
        fields = "__all__"

        widgets = {
            "shop_owner": forms.TextInput(attrs={"class": "form-control"}),
            "electronic_items": forms.Select(attrs={"class": "form-control"}),
            "item_price": forms.NumberInput(attrs={"class": "form-control"}),
            "shop_address": forms.TextInput(attrs={"class": "form-control"}),
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_mobile_no": forms.NumberInput(),
            "shop_opening_date": forms.DateInput(attrs={"type": "date"}),
        }
