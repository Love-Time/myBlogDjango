from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('posts/', Posts.as_view(), name='posts'),
    path('posts/category/<int:category_id>/', Posts_Category.as_view(), name='post_category'),

]
