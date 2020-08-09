from django import forms


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
