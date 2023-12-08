from django.urls import include, path
from . import views

app_name='Calendar'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/event/new/', views.event, name='event_new'),
    path('calendar/event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
]
