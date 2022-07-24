from django import forms


class FormularioContacto(forms.Form):

    nombre= forms.CharField(label="nombre",required=True)
    mail= forms.CharField(label="mail",required=True)
    contenido=forms.CharField(label="contenido",widget=forms.Textarea)