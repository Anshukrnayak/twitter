from django import forms
from .models import PostThread

class TreadForm(forms.ModelForm):
    class Meta:
        model=PostThread
        fields=['name','image','text_content']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control border-secondary'}),
            'text_content':forms.Textarea(attrs={'class':'form-control border-secondary'})
        }