from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="qwerty12",
            years_of_experience=3
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="qwerty12",
            years_of_experience=3
        )

    def test_experience_in_list(self):

        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)

    def test_years_of_experience_in_cook_detail_page(self):

        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)
