from django import forms
from .models import User


class StudentReg(forms.ModelForm):
    # re_password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['studentName', 'email', 'password', 'rePassword']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        rePassword = cleaned_data.get('rePassword')

        if password != rePassword:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    
class TeacherReg():
    class Meta(StudentReg.Meta):
        fields = ['teachername', 'email', 'password', 'rePassword']




   


