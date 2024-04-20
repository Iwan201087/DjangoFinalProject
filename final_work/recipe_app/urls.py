from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, recipe_detail, add_recipe, edit_recipe, user_login, user_logout, register


urlpatterns = [
    path('', index, name='index'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/', add_recipe, name='add_recipe'),
    path('recipe/edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)