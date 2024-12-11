from django import forms
from .models import CustomUser

class ProfileEditForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super(ProfileEditForm, self).__init__(*args, **kwargs)

       for field in self.fields.values():
           field.widget.attrs['class'] = 'form-control'

   class Meta:
       model = CustomUser
       fields = ('fullname','zipcode', 'address', 'phone')
       help_texts = {
           'fullname':'氏名',
           'zipcode': '郵便番号',
           'address': '住所',
           'phone': '電話番号',
       }