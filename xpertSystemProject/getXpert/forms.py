from django import forms
from .models import User
from django.contrib.auth import password_validation
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),required=True
    )
    confirm_password = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as before, for verification."),required=True
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        #for checking if email exits
        form_email = cleaned_data.get('email')
        confirm_password = cleaned_data.get('confirm_password')
        if User.objects.filter(email=form_email).exists():
	        raise forms.ValidationError('email id already exists. Please choose another email')
        if password != confirm_password:
            raise forms.ValidationError('password and confirm password does not match')



