from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms, BooleanField, BaseInlineFormSet

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = ['казино',
                       'криптовалюта',
                       'крипта',
                       'биржа',
                       'дешево',
                       'бесплатно',
                       'обман',
                       'полиция',
                       'радар']

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('view_counter', 'owner')

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        if any(word in name for word in self.forbidden_words):
            raise forms.ValidationError('Название продукта не должно содержать запрещенные слова.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        if any(word in description for word in self.forbidden_words):
            raise forms.ValidationError('Описание продукта не должно содержать запрещенные слова.')
        return description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
