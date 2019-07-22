from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.list_of_post, name='list_of_post'),
    path('<slug>/', views.post_detail, name="post_detail"),
    path('category/<category_slug>', views.list_of_post_by_category, name='list_of_post_by_category'),
    path('<slug>/comment/', views.add_comment, name='add_comment'),
    path('backend/post/new/', views.new_post, name="new_post"),
    path('backend/post/', views.list_of_post_backend, name="list_of_post_backend"),
    path('backend/<slug>/edit/', views.edit_post, name="edit_post"),
    path('backend/<slug>/delete/', views.delete_post, name="delete_post"),

    ]