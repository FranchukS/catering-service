from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Category, Dish

DISH_LIST_URL = reverse("kitchen:dish-list")
COOK_LIST_URL = reverse("kitchen:cook-list")
CATEGORY_LIST_URL = reverse("kitchen:category-list")

DISH_CREATE_URL = reverse("kitchen:dish-create")
COOK_CREATE_URL = reverse("kitchen:cook-create")
CATEGORY_CREATE_URL = reverse("kitchen:category-create")

HOME_PAGE_URL = reverse("kitchen:index")


class PublicTests(TestCase):
    def SetUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="qwerty12",
            years_of_experience=3
        )
        self.category = Category.objects.create(name="name")
        self.dish = Dish.objects.create(name="test", price="12.00", category_id=1)

    def test_dish_list(self):
        response = self.client.get(DISH_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_category_list(self):
        response = self.client.get(CATEGORY_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/category_list.html")

    def test_cook_list(self):
        response = self.client.get(COOK_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_index(self):
        response = self.client.get(HOME_PAGE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")

    def test_dish_create(self):
        response = self.client.get(DISH_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_category_create(self):
        response = self.client.get(CATEGORY_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_cook_create(self):
        response = self.client.get(COOK_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_category_search(self):
        response = self.client.get("/categories/?name=es")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["category_list"],
            Category.objects.filter(name__icontains="es")
        )

    def test_dish_search(self):
        response = self.client.get("/dishes/?name=es")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["dish_list"],
            Dish.objects.filter(name__icontains="es")
        )

    def test_cook_search(self):
        response = self.client.get("/cooks/?username=mi")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["cook_list"],
            get_user_model().objects.filter(username__icontains="mi")
        )


class PrivateTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="qwerty12",
            years_of_experience=3
        )
        self.category = Category.objects.create(name="Test")
        self.client.force_login(self.user)

    def test_retrieve_dish_list(self):
        Dish.objects.create(name="test", price="12.00", category_id=1)
        Dish.objects.create(name="test2", price="12.00", category_id=1)

        response = self.client.get(DISH_LIST_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dishes))

    def test_create_dish(self):
        form_data = {"name": "test3",
                     "price": "12.00",
                     "category_id": 1}

        self.client.post(reverse("kitchen:dish-create"), kwargs=form_data)

        new_dish = Dish.objects.get(name=form_data["name"])

        self.assertEqual(new_dish.name, form_data["name"])
        self.assertEqual(new_dish.price, form_data["price"])
        self.assertEqual(new_dish.category_id, form_data["category_id"])

    def test_create_cook(self):
        form_data = {
            "username": "user",
            "password1": "parol321",
            "password2": "parol321",
            "first_name": "Joe",
            "last_name": "Shmoe",
            "years_of_experience": 2,
        }

        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])

    def test_create_category(self):
        data = "Test"
        self.client.post(
            reverse("kitchen:category-create"),
            data={"name": data}
        )
        new_category = Category.objects.get(name=data)

        self.assertEqual(new_category.name, data)
