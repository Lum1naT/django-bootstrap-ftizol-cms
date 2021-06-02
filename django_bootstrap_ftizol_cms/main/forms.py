from django import forms


class WorkerAuthMailForm(forms.Form):
    username = forms.CharField(label='', max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label=(""), widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
