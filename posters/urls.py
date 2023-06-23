from django.urls import path
from .views import (
    PosterListView, 
    PosterDetailView, 
    SearchResultsListView, 
    PosterCreateView,
    # PosterUpdateView,
    # PosterDeleteView,
)


urlpatterns = [
    path('', PosterListView.as_view(), name='poster_list'), 
    path('create/', PosterCreateView.as_view(), name='poster_create'),
    path('<uuid:pk>/', PosterDetailView.as_view(), name='poster_detail'), 
    # path('<uuid:pk>/update/', PosterUpdateView.as_view(), name='poster_update'),
    # path('<uuid:pk>/delete/', PosterDeleteView.as_view(), name='poster_delete'),
    path('search/', SearchResultsListView.as_view(), name='poster_search_results'), 
]