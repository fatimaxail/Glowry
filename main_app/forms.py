from django.forms import ModelForm
from django import forms
from .models import Profile



class ProfileForm(forms.ModelForm):
    skin_concern = forms.MultipleChoiceField(
    choices = Profile._meta.get_field('skin_concern').base_field.choices,
    widget = forms.SelectMultiple,
    required = True,
    )
    skin_concern = forms.MultipleChoiceField(
    choices = Profile._meta.get_field('avoided_ingredients').base_field.choices,
    widget = forms.SelectMultiple,
    required = False,
    )



    class Meta:
        model = Profile
        fields = "__all__"

