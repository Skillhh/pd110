from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ['nombre','email']

    def clean_email(self): #Validacion Personalizada
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = email.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Correo no valido.")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje =  forms.CharField(widget=forms.Textarea)
