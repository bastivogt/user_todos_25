from django.db import models
from django.utils.translation import gettext as _
from django.contrib import admin
from django.urls import reverse
from tinymce import models as tinymce_models

from django.contrib.auth import get_user_model

User = get_user_model()





class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    name = models.CharField(max_length=150, verbose_name=_("Name"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def get_absolute_url(self):
        return reverse("todo_app:category_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = [
            "-updated"
        ]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")



class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    title = models.CharField(max_length=150, verbose_name=_("title"))
    # content = models.TextField(verbose_name="Content")
    content = tinymce_models.HTMLField(verbose_name=_("Content"))
    categories = models.ManyToManyField(Category, blank=True, related_name="todos", verbose_name=_("Categories"))
    done = models.BooleanField(default=False, verbose_name=_("Done"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def get_absolute_url(self):
        return reverse("todo_app:todo_detail", kwargs={"pk": self.id})


    def __str__(self):
        return f"{self.title} ({self.user.username})"
    
    
    @property
    @admin.display(description=_("Categories"))
    def categories_str(self):
        cats = self.categories.all()
        cats_list = [cat.name for cat in cats]
        print(cats_list)
        return ", ".join(cats_list)
    
    class Meta:
        ordering = [
            "done",
            "-updated"
        ]
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")
    

