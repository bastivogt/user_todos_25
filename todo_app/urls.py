from django.urls import path

from . import views

app_name = "todo_app"
urlpatterns = [
    #path("", views.index, name="index")
    path("todos/", views.TodoListView.as_view(), name="todo_index"),
    path("todo/detail/<int:pk>/", views.TodoDetailView.as_view(), name="todo_detail"),
    path("todo/create/", views.TodoCreateView.as_view(), name="todo_create"),
    path("todo/update/<int:pk>/", views.TodoUpdateView.as_view(), name="todo_update"),
    path("todo/delete/<int:pk>/", views.TodoDeleteView.as_view(), name="todo_delete"),

    path("todo/switch/done/<int:pk>/", views.todo_switch_done_list, name="todo_switch_done_list"),

    path("categories/", views.CategoryListView.as_view(), name="category_index"),
    
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category_create"),
    path("category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="category_update"),
    path("category/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="category_delete"),
    
]
