from django.urls import path
from .views import HomePageView, AboutPageView, SchedulePageView, ScheduleHistoryPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('schedule/', SchedulePageView.as_view(), name='schedule'),
    path('schedule_history/', ScheduleHistoryPageView.as_view(), name='schedule_history'), 
    # path('cover/', CoverPageView.as_view(), name='cover'),
    path('', HomePageView.as_view(), name='home'),
]
