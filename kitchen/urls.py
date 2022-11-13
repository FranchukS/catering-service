from django.urls import path

from kitchen.views import (
    index, CategoryListView,
    CategoryDetailView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView,
    CookListView, CookDetailView,
    CookCreateView, CookExperienceUpdateView,


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

]

app_name = "kitchen"
