from django import forms
from .models import CartItem

class AddToCartForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AddToCartForm, self).__init__(*args, **kwargs)

		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = CartItem
		fields = ['qty', 'product']

		widgets = {
			'qty': forms.NumberInput(attrs={
			'min': 1,
			'placeholder': '数量を入力してください',
			}),
			'product': forms.HiddenInput(),
		}