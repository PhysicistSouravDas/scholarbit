from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    list_display = ('title', 'author', 'date')    # The value of 'list_display' must not be a ManyToManyField.
    list_filter = ('author', 'date')
    search_fields = ('title',)                    # The value of 'list_filter' must be a list or tuple
    # raw_id_fields = ('author',)    # Enabling this, instead of author names, author id's will be shown in edit/create page of admin
    ordering = ('-date', 'title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'article', 'author')
    list_filter = ('author',)
    search_fields = ('comment',)


admin.site.register(Article, ArticleAdmin)