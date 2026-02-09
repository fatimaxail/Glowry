from django.contrib import admin
from django.urls import path
from . import views
from .views import profile
from .views import product_list, product_detail, add_review, edit_review, delete_review


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path("accounts/signup/", views.signup, name="signup"),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_count, name='profile'),


    path('articles/', views.ArticlesList.as_view(), name= "articles_index"),
    path('articles/<int:pk>/', views.ArticleDetails.as_view(), name= "articles_details"),
    path('articles/create/', views.ArticleCreate.as_view(), name= "articles_create"),
    path('articles/<int:pk>/update', views.ArticleUpdate.as_view(), name= "articles_update"),
    path('articles/<int:pk>/delete', views.ArticleDelete.as_view(), name= "articles_delete"),

    path('products/', product_list, name= "product_list"),
    path('products/search/', views.product_search, name='product_search'),
    path('products/<str:pk>', product_detail, name= "product_detail"),

    path("products/<str:pk>/review/", add_review, name="add_review"),
    path("reviews/<int:pk>/edit/", edit_review, name="edit_review"),
    path("reviews/<int:pk>/delete/", delete_review, name="delete_review"),

    path("routines/", views.routine_list, name="routinelist"),
    path("routines/<int:pk>/",  views.routine_detail, name="routine_detail"),
    path("routines/create", views.routine_create, name="routine_create"),
    path("routines/<int:pk>/edit",  views.routine_edit, name="routine_edit"),
    path("routines/<int:pk>/delete",  views.routine_delete, name="routine_delete"),

    path('routine/<int:routine_id>/add-product/', views.add_product_to_routine, name='add_product_to_routine'),
    path('routine_product/<int:pk>/edit/', views.edit_routine_product, name='edit_routine_product'),
    path('routine_product/<int:pk>/delete/', views.delete_routine_product, name='delete_routine_product'),
]

