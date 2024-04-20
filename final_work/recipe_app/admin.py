from django.contrib import admin
from django.contrib import admin
from .models import Recipe, CategoryRelationship, Category

admin.site.register(Recipe)

admin.site.register(Category)

admin.site.register(CategoryRelationship)
# Register your models here.

