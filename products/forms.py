from django import forms
from django.forms import fields
from products.models import Product


class StudentForm(forms.Form):
    roll_no = forms.IntegerField(
        label="TEst label", widget=forms.TextInput, error_messages={
            'blank': "Please enter a value"
        }, help_text="Please enter a unique no.")
    name = forms.CharField(max_length=150)
    height = forms.DecimalField()
    test = forms.DateField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['slug']
