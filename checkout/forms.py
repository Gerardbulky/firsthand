from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'email',
                  'street_address', 'postal_code', 'town', 'city', 'country',
                  ]


def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email Address',
        'phone_number': 'Phone Number',
        'street_address': 'Street Address',
        'postal_code': 'Postal Code',
        'town': 'Town',
        'city': 'City',
        'country': 'Country',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if field != 'country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
