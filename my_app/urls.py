from django.urls import path
from .views import  create_todo, get_todo, update_todo, delete_todo
# test_mongodb_connection,
urlpatterns = [
    path('todo/create/', create_todo, name='create_todo'),
    path('todo/get/', get_todo, name='get_todo'),
    path('todo/<str:pk>/update/', update_todo, name='update_todo'),
    path('todo/<str:pk>/delete/', delete_todo, name='delete_todo'),
    # path('test-mongo/', test_mongodb_connection, name='test_mongo'),
]
