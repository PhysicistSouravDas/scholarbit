from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article, Comment

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    query_pk_and_slug = True

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'
    #def test_func for UserPassesTestMixin
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    success_message = 'Article was updated successfully!'        

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    success_message = 'Article was deleted successfully!'

class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    fields = ('title', 'body')  #removed 'author' and added def form_valid() below
    template_name = 'article_new.html'
    login_url = 'login' #for LoginRequiredMixin, overriding default login url at accounts/login
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_message = 'Article was created successfully!'    

#Now for the feature of adding comments on listview and detailview of articles
class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    fields = ('comment',)
    template_name = 'comment_new.html'
    login_url = 'login'
    query_pk_and_slug = True
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    success_message = 'Comment was posted successfully!'    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    fields = ('comment',)
    template_name = 'comment_edit.html'
    login_url = 'login'
    #def test_func for UserPassesTestMixin
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    success_message = 'Comment was updated successfully!'


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    success_message = 'Comment was deleted successfully!'    