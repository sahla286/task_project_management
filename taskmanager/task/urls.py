from django.urls import path
from .views import DashboardView,AddView,DeleteTaskView,EditTaskView

urlpatterns = [
    path('dashboard',DashboardView.as_view() ,name='dash'),
    path('add',AddView.as_view(),name='add'),
    path('delete/<int:id>',DeleteTaskView.as_view(),name='delete'),
    path('edit/<int:id>',EditTaskView.as_view(),name='edit')
]