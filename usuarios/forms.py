from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm): 
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Senha', help_text='Obrigadorio 8 a 20 caracteres, Letras Maiusculas é minusculas, numeros e caracteres especiais')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(), label='Confirmação Senha')
    #nome = forms.CharField(required=True, label='Nome', widget=forms.TextInput())
   # email = forms.CharField(required=True, label='E-mail')
    class Meta:
      model = User
      fields = ('username','email','password', 'password2')
      
    