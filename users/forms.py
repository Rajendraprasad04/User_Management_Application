from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone
