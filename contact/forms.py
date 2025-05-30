from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder': 'Nombre'}), max_length=100, min_length=4)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder': 'Email'}), max_length=100, min_length=4)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Escribe tu mensaje', 'rows': 4, 'cols': 40}), max_length=1000, min_length=4)
    # widget=forms.Textarea es para que el campo de texto sea más grande
   