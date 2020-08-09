from django import forms

from .models import Message

class ContactForm(forms.Form):
    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(
        choices=[
            ("", '---------'),
            ('question', 'Pytanie'),
            ('opinion', "Opinia")
        ],
        label="Kategoria"
    )
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(widget=forms.Textarea, label="Treść", required=True)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        labels = {
            "name": "Imię",
            "email": "Email",
            "category": "Kategoria",
            "subject": "Tytuł",
            "body": "Treść"
        }
