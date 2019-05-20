from django import forms
from django.forms import widgets


# from drchrono.models import Paitent
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


class CheckinForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    # self.helper = FormHelper()
    # self.helper.form_method = 'post'
    # self.helper.add_input(Submit('submit', 'ckeckin'))
