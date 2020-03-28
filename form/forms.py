from django import forms

class PropertyForm(forms.Form):
    property = forms.CharField(label='property',max_length=20,widget=forms.TextInput)
