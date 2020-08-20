from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm, UserProfileForm
from .models import CustomUser
from articles.models import Article

# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = 'Account was created successfully! Now Log In using your details.'

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug' : self.object.username})
    template_name = 'profile_update.html'
    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user.username

    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return 'username'        
    success_message = "Account was updated successfully"    

class ProfileView(DetailView):
    model = CustomUser
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
            context = super(ProfileView, self).get_context_data(**kwargs)
            context['article_list'] = Article.objects.all()
            context['articles_by_user_list'] = Article.objects.filter(author=self.get_object()) #.request.user)
            context['article_count'] = Article.objects.filter(author=self.get_object()).count()
            # context['venue_list'] = Venue.objects.all()
            # context['festival_list'] = Festival.objects.all()
            # And so on for more models
            return context

    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return 'username'    
