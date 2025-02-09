from django.urls import path

from . import views

app_name = "todo_app"
urlpatterns = [
    #path("", views.index, name="index")
    path("", views.TodoListView.as_view(), name="todo_index"),
    path("detail/<int:pk>/", views.TodoDetailView.as_view(), name="todo_detail"),
    path("create/", views.TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", views.TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", views.TodoDeleteView.as_view(), name="todo_delete"),

    path("categories/", views.CategoryListView.as_view(), name="category_index"),
    
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category_create"),
    path("category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="category_update"),
    path("category/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="category_delete"),
    
]
