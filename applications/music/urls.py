# custom urls

from django.urls import path

from applications.music.views import *

urlpatterns = [
    path('musics/', get_music),
    path('music-detail/<int:id>/', misic_detail),
    path('task-create/', task_create),
    path('task-edit/<int:id>/', task_edit),
    path('task-delete/<int:pk>/', task_delete),
    path('', api_overview_links),

    path('l/', MovieListView.as_view()),
    path('c/', MovieCreateView.as_view()),
    path('d/<int:pk>/', MovieDeleteView.as_view()),
    path('detail/<str:title>/', MovieDetailView.as_view()),
    path('u/<int:pk>/', MovieUpdateView.as_view()),
    path('f/<int:pk>/', CommentListCreateView.as_view())

]

