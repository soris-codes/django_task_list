from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>', views.todo_view, name='todo_view'),
    path('new', views.todo_create, name='todo_new'),
    path('edit/<int:pk>', views.todo_update, name='todo_edit'),
    path('delete/<int:pk>', views.todo_delete, name='todo_delete'),
]