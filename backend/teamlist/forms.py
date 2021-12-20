from django import forms
from django.forms import ModelForm
from .models import TeamMember

class MemberForm(ModelForm):
    class Meta:
        model=TeamMember
        widgets =  {
            'first_name': forms.TextInput(attrs={'placeholder':'Charlene'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Pham'}),
            'email':forms.EmailInput(attrs={'placeholder':'charlene@instawork.com'}),
            'phone':forms.TextInput(attrs={'placeholder':'415-310-1619'}),
            'user_type':forms.RadioSelect()
        }
        fields = '__all__'

    
    
