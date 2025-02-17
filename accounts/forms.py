from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from accounts.models import SecurityQuestion


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert"> {e}</div>' for e in self]))
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        securityquestion = forms.CharField(label="What is the name of your first pet?", max_length=250, required=True)
        for fieldname in ['username', 'password1',
        'password2','securityQuestion']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )
class SecurityQuestionForm(forms.Form):
    SecurityQuestion = forms.CharField(label="What is the name of your first pet?", max_length=250)
    def save(self):
        pass
