from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.utils.translation import gettext as _
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Todo, Category
from .forms import CategoryForm, TodoForm

# Create your views here.

# Category

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "todo_app/category_index.html"
    login_url = reverse_lazy("sevo_user:sign_in")

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": _("All Categories")
        })
        return ctx
    

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    login_url = reverse_lazy("sevo_user:sign_in")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        todos = self.get_object().todos.all().filter(user=self.request.user)
        # print(todos)
        ctx.update({
            "todos": todos
        })
        return ctx
    
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("todo_app:category_index")
    login_url = reverse_lazy("sevo_user:sign_in")

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            "user": self.request.user
        })
        return initial
    
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("todo_app:category_index")
    login_url = reverse_lazy("sevo_user:sign_in")


    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            "user": self.request.user
        })
        return initial



class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "todo_app/category_confirm_delete.html"
    success_url = reverse_lazy("todo_app:category_index")
    login_url = reverse_lazy("sevo_user:sign_in")


    

# Todo

class TodoListView(LoginRequiredMixin, ListView):
    template_name = "todo_app/todo_index.html" # default todo_app/todo_list.html
    model = Todo
    login_url = reverse_lazy("sevo_user:sign_in")
    

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": _("All Todos")
        })
        return ctx
    


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = "todo_app/todo_detail.html"
    login_url = reverse_lazy("sevo_user:sign_in")
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(user=self.request.user)
    

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_app:todo_index")
    login_url = reverse_lazy("sevo_user:sign_in")

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            "user": self.request.user,
            #"categories": Category.objects.all().filter(user=self.request.user)
        })
        return initial
    
    def get_form_kwargs(self):
        fk = super().get_form_kwargs()
        fk["user"] = self.request.user
        return fk
    


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_app:todo_index")

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            "user": self.request.user
        })
        return initial
    
    def get_form_kwargs(self):
        fk = super().get_form_kwargs()
        fk["user"] = self.request.user
        return fk
    

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "todo_app/todo_confirm_delete.html"
    success_url = reverse_lazy("todo_app:todo_index")
    login_url = reverse_lazy("sevo_user:sign_in")



@login_required(login_url="sevo_user:sign_in")
def todo_switch_done_list(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.done = not todo.done
        todo.save()
    return render(request, "todo_app/partials/_todo-list.html", {
        "todo_list": Todo.objects.filter(user=request.user)
    })


@login_required(login_url="sevo_user:sign_in")
def todo_switch_done_single(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.done = not todo.done
        todo.save()
    return render(request, "todo_app/partials/_todo-item-detail.html", {
        "todo": todo
    })

    

    
    


    



    



    


