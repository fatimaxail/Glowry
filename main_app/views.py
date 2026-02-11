import os, json
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, Review, Routine, RoutineProduct
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.views.generic import ListView, DetailView
from .forms import ReviewForm, RoutineForm, RoutineProductForm, ProfileForm, AddRoutineProductForm
from django.contrib.auth.models import User
from django.db import transaction

# Create your views here.

CATEGORY_ORDER = {
    "Oil Cleanser": 1,
    "Cleanser": 2,
    "Exfoliant": 3,
    "Toner": 4,
    "Essence": 5,
    "Serum": 6,
    "Moisturizer": 7,
    "Sunscreen": 8,
    "Eye Care": 9,
    "Lip Care": 10,
    "Mask": 11
}


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("profile_edit")
        else:
            error_message = "Invalid signup - try again"

    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)

@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "users/profile_edit.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def profile_count(request, username):
    profile_user = User.objects.annotate(
    review_count=Count('review'),
    article_count=Count('article')
    ).get(username=username)

    return render(request, 'users/profile.html', {'user': profile_user})


class ArticlesList(LoginRequiredMixin, ListView):
    model = Article


class ArticleDetails(LoginRequiredMixin, DetailView):
    model = Article


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["title", "image", "content", "reading_time"]
    success_url = "/articles/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = "__all__"
    success_url = "/articles/"


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = "/articles/"


@login_required
def product_list(request):
    json_path = os.path.join(
        settings.BASE_DIR, "main_app", "data", "skincare_products.json"
    )

    with open(json_path, "r") as file:
        products = json.load(file)

    return render(
        request, "products/list.html", {"products": products["skincare_products"]}
    )

@login_required
def product_search(request):
    query = request.GET.get("query", None)

    json_path = os.path.join(
        settings.BASE_DIR, "main_app", "data", "skincare_products.json"
    )

    with open(json_path, "r") as file:
        products = json.load(file)["skincare_products"]

    query = query.lower()

    filtered_products = [
        product for product in products
        if query in product.get("name", "").lower()
        or query in product.get("brand", "").lower()
        or query in product.get("category", "").lower()
        or any(query in ingredient.lower() for ingredient in product.get("ingredients", []))
    ]

    return render(
        request,
        "products/list.html",
        {"products": filtered_products}
    )



@login_required
def product_detail(request, pk):

    json_path = os.path.join(
        settings.BASE_DIR, "main_app", "data", "skincare_products.json"
    )
    with open(json_path, "r") as file:
        data = json.load(file)

    products = data["skincare_products"]

    product = next((product for product in products if product["id"] == pk), None)


    review_form = ReviewForm()
    reviews = Review.objects.filter(product_id = pk)

    return render(
        request, "products/details.html", {"product": product, "review_form": review_form, "reviews": reviews}
        )


@login_required
def add_review(request, pk):
    form = ReviewForm(request.POST, request.FILES)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.product_id = pk
        new_review.user = request.user
        new_review.save()

    return redirect("product_detail", pk=pk)


@login_required
def edit_review(request, pk):
    review = Review.objects.get(id=pk)

    if review.user != request.user:
        return redirect("product_detail", pk=review.product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=review.product_id)

    else:
        form = ReviewForm(instance=review)

    return render(
        request, "products/edit_review.html", {"form": form, "review": review}
    )


@login_required
def delete_review(request, pk):
    review = Review.objects.get(id=pk)

    if review.user != request.user:
        return redirect("product_detail", pk=review.product_id)

    product_id = review.product_id
    review.delete()

    return redirect("product_detail", pk=product_id)


@login_required
def routine_create(request):
        if request.method == "POST":
            form = RoutineForm(request.POST)
            if form.is_valid():
                new_routine = form.save(commit=False)
                new_routine.user = request.user
                new_routine.save()
                return redirect("routine_detail", pk=new_routine.id)
        else:
            form = RoutineForm()

        return render(request, "routine/form.html", {"form": form})


@login_required
def routine_list(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, "routine/list.html", {"routines": routines})

@login_required
def routine_detail(request, pk):
    routine = Routine.objects.get(id=pk)

    json_path = os.path.join(
        settings.BASE_DIR, "main_app", "data", "skincare_products.json"
    )

    with open(json_path, "r") as file:
        data = json.load(file)["skincare_products"]

    all_routine_products = RoutineProduct.objects.filter(routine=routine)

    routine_products = []
    for item in all_routine_products:
        product_data = next(( product for product in data if product['id'] == item.product_id), None)

        if product_data:
            product_data = product_data.copy()
            product_data['time'] = item.time
            product_data['frequency'] = item.get_frequency_display() if hasattr(item, 'get_frequency_display') else item.frequency
            product_data['priority'] = CATEGORY_ORDER.get(product_data.get('category'), 99)
            product_data["db_id"] = item.id
            routine_products.append(product_data)

    routine_products.sort(key=lambda x: x["priority"])

    return render(
        request, "routine/detail.html", {"routine": routine, "products": routine_products}
    )


@login_required
def routine_edit(request, pk):
    routine = Routine.objects.get(id=pk)

    if request.method == "POST":
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            return redirect("routinelist")
    else:
        form = RoutineForm(instance=routine)
    return render(request, "routine/form.html", {"form": form})


@login_required
def routine_delete(request, pk):
    routine = Routine.objects.get(id=pk)
    if request.method == "POST":
        routine.delete()
        return redirect("routinelist")
    return render(request, "routine/delete_confirm.html", {"routine": routine})

def add_product_to_routine(request, routine_id):
    routine = Routine.objects.get(id=routine_id)

    json_path = os.path.join(settings.BASE_DIR, "main_app", "data", "skincare_products.json")

    with open(json_path, "r") as file:
        data = json.load(file)["skincare_products"]

    choices = [(product['id'], product['name']) for product in data]

    if request.method == "POST":
        form = AddRoutineProductForm(request.POST, product_choices=choices)
        if form.is_valid():
            routine_product = form.save(commit=False)
            routine_product.routine = routine
            routine_product.save()
            return redirect('routine_detail', pk=routine_id)
    else:
        form = AddRoutineProductForm(product_choices=choices)

    return render(request, 'routine/add_product.html', {'form': form, 'routine': routine, 'products': data})


@login_required
def edit_routine_product(request, pk):
    routine_product = RoutineProduct.objects.get(id=pk, routine__user=request.user)

    json_path = os.path.join(settings.BASE_DIR, "main_app", "data", "skincare_products.json")
    with open(json_path, "r") as file:
        data = json.load(file)["skincare_products"]

    display_product = next((product for product in data if product['id'] == routine_product.product_id), None)

    if request.method == "POST":
        form = RoutineProductForm(request.POST, instance=routine_product)
        if form.is_valid():
            form.save()
            return redirect('routine_detail', pk=routine_product.routine.id)
    else:
        form = RoutineProductForm(instance=routine_product)

    return render(request, 'routine/edit_product.html', {
        'form': form,
        'routine_product': routine_product,
        'display_product': display_product
    })



@login_required
def delete_routine_product(request, pk):
    product = RoutineProduct.objects.get(id=pk, routine__user=request.user)
    routine_id = product.routine.id
    product.delete()
    return redirect('routine_detail', pk=routine_id)
