from django.test import TestCase

from kitchen.models import Dish, Category, Cook


class ModelsTests(TestCase):
    def test_dish_str(self):
        Category.objects.create(name="test")
        dish = Dish.objects.create(name="test", price="12.00", category_id=1)
        self.assertEqual(str(dish), dish.name)

    def test_cook_str(self):
        cook = Cook.objects.create_user(
            username="test",
            password="qwerty1",
            first_name="test first",
            last_name="test last",
            years_of_experience=2
        )

        self.assertEqual(
            str(cook),
            f"{cook.first_name} {cook.last_name}"
        )

    def test_add_experience_to_cook(self):
        username = "test"
        password = "qwerty1"
        experience = 2
        cook = Cook.objects.create_user(
            username=username,
            password=password,
            years_of_experience=experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, experience)

    def test_category_str(self):
        category = Category.objects.create(name="test")
        self.assertEqual(str(category), category.name)
