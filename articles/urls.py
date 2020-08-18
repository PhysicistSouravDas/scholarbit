from django.urls import path
from .views import (ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView, 
                    CommentCreateView, CommentUpdateView, CommentDeleteView)

urlpatterns = [
    path('<int:pk>/<str:slug>/comment/', CommentCreateView.as_view(), name='comment_new'),
    path('<int:pk>/comment_edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('<int:pk>/comment_delete/', CommentDeleteView.as_view(), name='comment_delete'),
    #Articles below
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:slug>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/<str:slug>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    
]
