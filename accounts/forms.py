from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from accounts.models import SecurityQuestion
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert"> {e}</div>' for e in self]))


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

class SecurityQuestionForm(forms.ModelForm):
    class Meta:
        model = SecurityQuestion
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(SecurityQuestionForm, self).__init__(*args, **kwargs)
        self.fields['answer'].label = "What\'s your favorite color?"
        for fieldname in ['answer']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    securityQuestion = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = "New password"
        self.fields['securityQuestion'].label = "What\'s your favorite color?"
        for fieldname in ['username', 'password', 'securityQuestion']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        answer = cleaned_data.get("securityQuestion")

        if not User.objects.filter(username=username).exists():
            raise ValidationError("Username doesn't exist")

        user = User.objects.get(username=username)
        if answer != str(user.securityquestion):
            raise ValidationError("Incorrect answer to security question")