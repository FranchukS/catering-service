from django.shortcuts import render

from kitchen.models import Cook, Dish, Category


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_categories = Category.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_categories": num_categories,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)