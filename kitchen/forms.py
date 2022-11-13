from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience", "email", "first_name", "last_name",
        )