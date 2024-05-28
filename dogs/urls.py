from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from dogs.apps import DogsConfig
from dogs.views import IndexView, CategoryListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView

app_name = DogsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/',cache_page(60) (CategoryListView.as_view()), name='categories'),
    path('dogs/<int:pk>/',cache_page(60) ( DogListView.as_view()), name='category'),
    path('<int:pk>/dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>/', never_cache(DogUpdateView.as_view()), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),


]