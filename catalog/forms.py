from django import forms
from catalog.models  import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите названия продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Опишите продукт'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })



    forbidden_words =[
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар',
    ]


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '').lower()
        description = cleaned_data.get('description', '').lower()

        for word in self.forbidden_words:
            if word in name:
                self.add_error('name', f'Название содержит запрещённое слово: "{word}"')
            if word in description:
                self.add_error('description', f'Описание содержит запрещённое слово: "{word}"')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price




