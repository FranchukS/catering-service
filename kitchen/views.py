from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, CookExperienceUpdateForm, DishForm, SearchForm
from kitchen.models import Cook, Dish, Category


def index(request):

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


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 5
    queryset = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("username", "")

        context["search_form"] = SearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class CategoryDetailView(generic.DetailView):
    model = Category
    queryset = Category.objects.all().prefetch_related("dishes")


class CategoryCreateView(generic.CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("kitchen:category-list")


class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("kitchen:category-list")


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy("kitchen:category-list")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = Cook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = SearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(username__icontains=name)
        return self.queryset


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__category")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CookCreationForm
    template_name = "kitchen/cook_form.html"


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = SearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.prefetch_related("cooks")


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = DishForm
    template_name = "kitchen/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


@login_required
def assign_or_discharge(request, pk):
    dish = Dish.objects.get(pk=pk)
    user = request.user
    if user in dish.cooks.all():
        dish.cooks.remove(user.id)
    else:
        dish.cooks.add(user.id)

    return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", args=[dish.id]))
