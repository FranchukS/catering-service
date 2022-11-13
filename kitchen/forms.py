from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish


class ExperienceValidateMixin:
    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]

        if years_of_experience < 0:
            raise ValidationError(
                "Experience can't be lower then 0"
            )

        if years_of_experience > 50:
            raise ValidationError(
                "Invalid input max value is 50"
            )

        return years_of_experience


class CookCreationForm(ExperienceValidateMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience", "email", "first_name", "last_name",
        )


class CookExperienceUpdateForm(ExperienceValidateMixin, forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_of_experience",)


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )
