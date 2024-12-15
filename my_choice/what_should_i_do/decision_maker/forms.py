from django import forms
from .models import DecisionOption

class DecisionOptionForm(forms.ModelForm):
    class Meta:
        model = DecisionOption
        fields = ['category', 'option']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'option': forms.TextInput(attrs={'placeholder': 'Your Decision Option', 'class': 'form-control'}),
        }
