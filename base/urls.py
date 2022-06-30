from unicodedata import name
from django.urls import path

from .views import TaskList ,TaskDetail , TaskCreate,TaskUpdate,DeleteView


urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='task-create'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('delete-task/<int:pk>/',DeleteView.as_view(),name='task-delete'),
    

]
