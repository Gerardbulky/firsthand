from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id) for c in categories]

        self.fields['name'].choices = friendly_names
        for field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


  