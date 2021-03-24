from django import forms 
from authe.models import Author

class Register(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['username', 'email', 'password',]

class LoginForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = ('username', 'password')


        