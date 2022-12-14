from django.urls import path

from kitchen.views import (
    index, CategoryListView,
    CategoryDetailView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView,
    CookListView, CookDetailView,
    CookCreateView, CookExperienceUpdateView,
    CookDeleteView, DishListView,
    DishDetailView, DishCreateView,
    DishUpdateView, DishDeleteView,
    assign_or_discharge
)


urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/experience-update/",
         CookExperienceUpdateView.as_view(), name="experience-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),

    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/<int:pk>/assign-or-discharge/", assign_or_discharge, name="assign-or-discharge"),
]

app_name = "kitchen"
