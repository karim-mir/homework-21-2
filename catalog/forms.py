from django import forms
from django.forms import ModelForm, BooleanField
from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар"
]

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        if name:
            self.validate_forbidden_words(name)
        if description:
            self.validate_forbidden_words(description)
        return cleaned_data

    def validate_forbidden_words(self, value):
        for word in FORBIDDEN_WORDS:
            if word.lower() in value.lower():
                raise forms.ValidationError(f"Слово '{word}' запрещено использовать.")

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        elif price is not None and price == 0:
            raise forms.ValidationError("Цена не может быть равна нулю.")

        return price


class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    email = forms.EmailField(label="Ваш email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)
