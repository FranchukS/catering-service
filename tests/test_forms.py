from django.test import TestCase

from kitchen.forms import CookCreationForm, CookExperienceUpdateForm


class FormsTest(TestCase):
    def test_cook_creation_form_with_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "tester",
            "password1": "parol123",
            "password2": "parol123",
            "email": "Joe@a.com",
            "first_name": "Joe",
            "last_name": "Shmoe",
            "years_of_experience": 2
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_update_experience_form_is_valid(self):
        form_data = {"years_of_experience": 2}

        form = CookExperienceUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
