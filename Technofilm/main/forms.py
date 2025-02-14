from django import forms
 
class UserForm(forms.Form):
    value = forms.CharField(widget=forms.TextInput(attrs={"class":"inputField"}), required=False)