from django.forms import ModelForm
from django import forms
from .models import Profile, Review, Routine, RoutineProduct



class ProfileForm(forms.ModelForm):
    skin_concern = forms.MultipleChoiceField(
    choices = Profile._meta.get_field('skin_concern').base_field.choices,
    widget = forms.SelectMultiple,
    required = True,
    )
    avoided_ingredients = forms.MultipleChoiceField(
    choices = Profile._meta.get_field('avoided_ingredients').base_field.choices,
    widget = forms.SelectMultiple,
    required = False,
    )


    class Meta:
        model = Profile
        fields = ["avatar", "bio", "age", "skin_type", "skin_concern", "avoided_ingredients" ]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review_description", "image"]

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description']


class AddRoutineProductForm(forms.ModelForm):
    class Meta:
        model = RoutineProduct
        fields = ['product_id', 'time', 'frequency']
        widgets = {
            'time': forms.Select(),
            'frequency': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        product_choices = kwargs.pop('product_choices', [])
        super(AddRoutineProductForm, self).__init__(*args, **kwargs)
        self.fields['product_id'].choices = product_choices

class RoutineProductForm(forms.ModelForm):
    class Meta:
        model = RoutineProduct
        fields = ['frequency']


