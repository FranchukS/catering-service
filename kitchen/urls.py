from django.urls import path

from kitchen.views import (
    index, CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),

]

app_name = "kitchen"
