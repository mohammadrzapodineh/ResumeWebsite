from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=110, widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'متن'}))