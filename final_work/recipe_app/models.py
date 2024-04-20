from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_method = models.TextField()
    cooking_time = models.PositiveIntegerField()
    cooking_product = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    
    def __str__(self) -> str:
        return self.title
                
                
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
                

class CategoryRelationship(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    class Meta:
        unique_together = ['recipe', 'category']
# Create your models here.