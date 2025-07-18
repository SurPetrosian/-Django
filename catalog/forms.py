from django import forms
from catalog.models  import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']

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
