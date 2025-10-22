# contacts/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # 'owner' is set automatically in the view, so we exclude it from the form
        fields = ['name', 'email', 'phone', 'address']