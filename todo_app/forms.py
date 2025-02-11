from django import forms
from tinymce.widgets import TinyMCE

from .models import Category, Todo

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
        exclude = [
            "user"
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }




class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        
        self.fields["categories"].queryset = Category.objects.filter(user=user)

    def get_sevo(self):
        return "SEVO"


    class Meta:
        model = Todo
        fields = "__all__"
        exclude = [
            "user"
        ]

        #widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": TinyMCE(attrs={"cols": 80, "rows": 30, "class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-select multiple"}),
            "done": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }