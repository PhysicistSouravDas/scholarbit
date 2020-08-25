from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Importing Articles and User model for search view
from articles.models import Article
from django.contrib.auth import get_user_model
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class FeaturesPageView(TemplateView):
    template_name = 'features.html'

class AnnouncementsPageView(TemplateView):
    template_name = 'announcements.html'

#Search View Below
Users = get_user_model()
class SearchResultsView(ListView):
    model = Article
    template_name = "search_results.html"
    # The template is in users/templates/search_results.html

    def get_context_data(self):
        query = self.request.GET.get('q')
        if '@' in query:
            modified_query = query[1:]
            if ' '  in modified_query:
                queried_first_name = modified_query[:modified_query.index(' ')]
                queried_last_name =  modified_query[modified_query.index(' ') + 1:]
                search_list = Users.objects.filter(
                    Q(first_name__icontains = queried_first_name) | 
                    Q(last_name__icontains = queried_last_name)
                )
            else:
                search_list = Users.objects.filter(
                    Q(first_name__icontains = modified_query) | 
                    Q(last_name__icontains = modified_query) | 
                    Q(username__icontains = modified_query)
            )
        else:
            search_list = Article.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
                )
        ctx = {
            'search_list': search_list, 
            'query':  query, 
            'search_count': search_list.count()
            }
        return ctx