from django.urls import path
from api import views

urlpatterns = [
    path('resume/', views.ProfileView.as_view(), name='resume'),
    path('list/', views.ProfileView.as_view(), name='list'),
    path('all/', views.ProfileView.as_view(), name='all'),
    # path('resume/<int:pk>/', views.ProfileView.as_view(), name='resume-update'),
    # path('resume/', views.ProfileListView.as_view(), name='resume-list-create'),
    path('resume/<int:pk>/', views.ProfileDetailView.as_view(), name='resume-detail-update-delete'),


]
