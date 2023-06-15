from django import forms
from .models import EmailMobileUser

class EmailMobileUserForm(forms.ModelForm):
    class Meta:
        model = EmailMobileUser
        fields = '__all__'
        
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        print(len(mobile))
        # Perform your custom validation logic here
        if not mobile.startswith('+91'):
            raise forms.ValidationError("Mobile number must start with '+'")
        if len(mobile)<10:
             raise forms.ValidationError("Mobile number must 10 digit")
        return mobile