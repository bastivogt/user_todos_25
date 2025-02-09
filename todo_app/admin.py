from django.contrib import admin

from .models import Category, Todo

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "name",
        "created",
        "updated",
    ]

    list_display_links = [
        "id", 
        "name",
        "user"
    ]



class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "done",
        "user",
        "categories_str",
        "created",
        "updated"
    ]

    list_display_links = [
        "id", 
        "title"
    ]

    readonly_fields = [

    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Todo, TodoAdmin)
