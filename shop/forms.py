from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form__input', 'type': "text", 'placeholder': "Напишите ваше имя"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form__input', 'type': "email", 'placeholder': "Напишите адрес вашей почты"}))
    number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form__input', 'placeholder': "99 8(хх) ххх-хх-хх "}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form__input', 'placeholder': "Напишите сообщение..."}))
