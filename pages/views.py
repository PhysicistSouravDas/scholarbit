from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Importing Articles model for search view
from articles.models import Article
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
class SearchResultsView(ListView):
    model = Article
    template_name = "search_results.html"
    # The template is in users/templates/search_results.html

    def get_context_data(self):
        query = self.request.GET.get('q')
        search_list = Article.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
            )
        ctx = {'search_list': search_list}
        return ctx