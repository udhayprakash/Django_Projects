from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from ftp_to_db.models import FTPCredentials

class FTPCredentialsForm(forms.ModelForm):

    class Meta:
        model = FTPCredentials
        fields = ('ftp_url', 'ftp_username', 'ftp_password', 'ftp_filename')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'LoadToOurDB'))