from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook


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


