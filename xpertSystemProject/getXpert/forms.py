from django import forms
from .models import User
from django.contrib.auth import password_validation


class UserRegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    confirm_password = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        #for checking if email exits
        email = cleaned_data.get('email')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('password and confirm password does not match')