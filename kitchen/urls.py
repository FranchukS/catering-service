from django.urls import path

from kitchen.views import (
    index, CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
]

app_name = "kitchen"
