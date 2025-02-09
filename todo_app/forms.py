from django import forms

from .models import Category, Todo

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"




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