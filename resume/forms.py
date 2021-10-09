from django import forms
from django.forms import fields
from django.test import client
from . models import Acomplishment, Detail
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

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
        fields = "phone_number address profile_pic backgroud_pic about_me skills".split()

class AccomUpdateForm(forms.ModelForm):
    class Meta:
        model = Acomplishment
        fields = "work_completed years_of_exper total_client award_won".split()

class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
