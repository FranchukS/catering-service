from django.urls import path

from kitchen.views import index, CategoryListView

urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
]

app_name = "kitchen"
