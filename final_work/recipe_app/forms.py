from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_method', 'cooking_time', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'cooking_method': forms.Textarea(attrs={'class': 'form-control'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'cooking_method': 'Способ приготовления',
            'cooking_time': 'Время приготовления (в минутах)',
            'image': 'Изображение',
            'category': 'Категория',
        }