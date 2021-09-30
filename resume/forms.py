from django import forms
from django.forms import fields
from django.test import client
from . models import Acomplishment, Detail
from django.contrib.auth import get_user_model

User = get_user_model()

class SignInForm(forms.Form):
    username = forms.CharField(max_length=50,
                               label="Username"
                            )
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        # The iexact makes the query responed to case insensitive

        if not qs.exists():
            # exists method return a bool if or not if the query exist in the DB.
            raise forms.ValidationError(
                "Opps! Only Isaiah Olaoye can access this platform."
            )

        return username

class ProjectForm(forms.Form):
        name = forms.CharField(label='Project Name')
        topic = forms.CharField(label='Project Topic')
        description = forms.CharField(widget=forms.Textarea)
        proj_pic = forms.ImageField(label='Project Picture', required=True)
        proj_url = forms.URLField(label='URL')
        client = forms.CharField()
        created = forms.DateTimeField(label='Date Created')

# Because it's only me that has access to this view, 
# I don't need validation of any kind.
class DetailUpdateForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = "phone_number address profile_pic about_me skills".split()

class AccomUpdateForm(forms.ModelForm):
    class Meta:
        model = Acomplishment
        fields = "work_completed years_of_exper total_client award_won".split()

    
