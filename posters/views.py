from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin, 
)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Poster


class PosterListView(LoginRequiredMixin, ListView):
    model = Poster
    context_object_name = 'poster_list'
    template_name = 'posters/poster_list.html'
    login_url = 'account_login'


class PosterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Poster
    fields = [
        'title',
        'image', 
        'author', 
    ]
    template_name = 'posters/poster_create.html'
    login_url = 'account_login'
    permission_required = 'posters.is_starchaser2017'
    
    # redirect to the detail view of the newly created poster
    def get_success_url(self):
        return reverse_lazy('poster_detail', args=[self.object.id])


class PosterDetailView(
        LoginRequiredMixin, 
        PermissionRequiredMixin, 
        DetailView, 
    ):
    model = Poster
    context_object_name = 'poster'
    template_name = 'posters/poster_detail.html'
    login_url = 'account_login'
    permission_required = 'posters.is_starchaser2017'


class SearchResultsListView(ListView):
    model = Poster
    context_object_name = 'poster_list'
    template_name: str = 'posters/poster_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Poster.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query)
        )
