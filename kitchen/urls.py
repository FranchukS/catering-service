from django.urls import path

from kitchen.views import (
    index, CategoryListView,
    CategoryDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]

app_name = "kitchen"
